(function () {
  const HOVER_OPEN_DELAY = 100;
  const HOVER_CLOSE_DELAY = 150;
  const EASE = 'cubic-bezier(0.22, 1, 0.36, 1)';
  const DUR_MORPH = '350ms';
  const DUR_OPEN = '200ms';
  const DUR_CLOSE = '150ms';
  const SLIDE_PX = 60;

  // ---------- Desktop: single shared popup that morphs between items ----------
  const navRoot = document.querySelector<HTMLElement>('[data-nav-root]');
  const popup = document.querySelector<HTMLElement>('[data-nav-popup]');
  const viewport = document.querySelector<HTMLElement>('[data-nav-viewport]');
  const triggerBtns: HTMLElement[] = navRoot
    ? Array.from(navRoot.querySelectorAll<HTMLElement>('[data-nav-trigger-button]'))
    : [];
  const contentPanels: HTMLElement[] = navRoot
    ? Array.from(navRoot.querySelectorAll<HTMLElement>('[data-nav-content]'))
    : [];
  // All top-level nav items in visual order — dropdown triggers AND plain
  // links — so forward-Tab out of a popup can land on a plain link that
  // sits between dropdowns instead of skipping it.
  const topLevelItems: HTMLElement[] = navRoot
    ? Array.from(navRoot.querySelectorAll<HTMLElement>(':scope > ul > li > a[href], :scope > ul > li > button[data-nav-trigger-button]'))
    : [];

  let currentIdx = -1;
  let isOpen = false;
  let openTimer: number | null = null;
  let closeTimer: number | null = null;
  let panelSizes: { width: number; height: number }[] = [];

  // Pre-measure each panel's natural dimensions by temporarily exposing them off-screen.
  function measurePanels(): void {
    if (!popup || !viewport || contentPanels.length === 0) return;
    const ps = popup.style;
    const vs = viewport.style;

    const savedPopup = {
      display: ps.display,
      position: ps.position, left: ps.left, top: ps.top,
      width: ps.width, height: ps.height, overflow: ps.overflow,
      opacity: ps.opacity, transform: ps.transform,
      pointerEvents: ps.pointerEvents, transition: ps.transition,
    };
    const savedViewport = { overflow: vs.overflow, width: vs.width, height: vs.height };
    const savedContents = contentPanels.map(c => ({
      position: c.style.position,
      opacity: c.style.opacity,
      transform: c.style.transform,
    }));

    // Expose off-screen (display:block needed when initial state is display:none)
    ps.display = 'block';
    ps.position = 'fixed';
    ps.left = '-9999px';
    ps.top = '0';
    ps.width = 'auto';
    ps.height = 'auto';
    ps.overflow = 'visible';
    ps.opacity = '0';
    ps.transform = 'none';
    ps.pointerEvents = 'none';
    ps.transition = 'none';
    vs.overflow = 'visible';
    vs.width = 'auto';
    vs.height = 'auto';
    contentPanels.forEach(c => {
      c.style.position = 'static';
      c.style.opacity = '1';
      c.style.transform = 'none';
    });

    popup.offsetHeight; // force layout

    panelSizes = contentPanels.map(c => {
      // Measure the inner grid div which carries the explicit w-[Npx] — not the
      // wrapper, which stretches to the widest sibling when all panels are stacked.
      const inner = (c.firstElementChild as HTMLElement) ?? c;
      return { width: inner.offsetWidth, height: inner.offsetHeight };
    });

    // Restore
    contentPanels.forEach((c, i) => {
      c.style.position = savedContents[i].position;
      c.style.opacity = savedContents[i].opacity;
      c.style.transform = savedContents[i].transform;
    });
    vs.overflow = savedViewport.overflow;
    vs.width = savedViewport.width;
    vs.height = savedViewport.height;
    ps.display = savedPopup.display;
    ps.position = savedPopup.position;
    ps.left = savedPopup.left;
    ps.top = savedPopup.top;
    ps.width = savedPopup.width;
    ps.height = savedPopup.height;
    ps.overflow = savedPopup.overflow;
    ps.opacity = savedPopup.opacity;
    ps.transform = savedPopup.transform;
    ps.pointerEvents = savedPopup.pointerEvents;
    ps.transition = savedPopup.transition;
  }

  function setActiveTrigger(idx: number): void {
    triggerBtns.forEach((btn, i) => {
      if (i === idx) {
        btn.dataset.open = 'true';
        btn.setAttribute('aria-expanded', 'true');
      } else {
        delete btn.dataset.open;
        btn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // Slide new content in, old content out, rest hidden.
  // Non-active panels get pointer-events:none so their (invisible) stacked
  // children don't intercept clicks meant for the active panel, and `inert`
  // so their links are skipped by Tab and removed from the a11y tree.
  function slideContent(nextIdx: number, prevIdx: number): void {
    const dir = prevIdx >= 0 && prevIdx < nextIdx ? 1 : -1;
    contentPanels.forEach((c, i) => {
      if (i === nextIdx) {
        c.style.transition = 'none';
        c.style.opacity = '0';
        c.style.transform = `translateX(${dir * SLIDE_PX}px)`;
        c.style.pointerEvents = 'auto';
        c.removeAttribute('inert');
        c.offsetHeight; // reflow
        c.style.transition = `opacity ${DUR_MORPH} ${EASE}, transform ${DUR_MORPH} ${EASE}`;
        c.style.opacity = '1';
        c.style.transform = 'translateX(0)';
      } else if (i === prevIdx) {
        c.style.transition = `opacity ${DUR_MORPH} ${EASE}, transform ${DUR_MORPH} ${EASE}`;
        c.style.opacity = '0';
        c.style.transform = `translateX(${-dir * SLIDE_PX}px)`;
        c.style.pointerEvents = 'none';
        c.setAttribute('inert', '');
      } else {
        c.style.transition = 'none';
        c.style.opacity = '0';
        c.style.transform = 'translateX(0)';
        c.style.pointerEvents = 'none';
        c.setAttribute('inert', '');
      }
    });
  }

  function panelItems(idx: number): HTMLElement[] {
    const panel = contentPanels[idx];
    if (!panel) return [];
    return Array.from(panel.querySelectorAll<HTMLElement>('a[href], button:not([disabled])'));
  }

  function popupLeftFor(idx: number): number {
    if (!navRoot || !triggerBtns[idx]) return 0;
    const navRect = navRoot.getBoundingClientRect();
    const btnRect = triggerBtns[idx].getBoundingClientRect();
    let left = btnRect.left - navRect.left;
    if (panelSizes[idx]) {
      const overflow = left + panelSizes[idx].width - (window.innerWidth - navRect.left) - 16;
      if (overflow > 0) left = Math.max(0, left - overflow);
    }
    return left;
  }

  function openDropdown(idx: number): void {
    if (!popup || !panelSizes[idx]) return;
    const prevIdx = isOpen ? currentIdx : -1;
    const wasOpen = isOpen;
    currentIdx = idx;
    isOpen = true;
    setActiveTrigger(idx);
    slideContent(idx, prevIdx);

    const sz = panelSizes[idx];
    const left = popupLeftFor(idx);
    const ps = popup.style;

    if (!wasOpen) {
      // Initial open: snap size/position, then fade + scale in
      ps.transition = 'none';
      ps.display = 'block';
      ps.left = `${left}px`;
      ps.width = `${sz.width}px`;
      ps.height = `${sz.height}px`;
      ps.opacity = '0';
      ps.transform = 'scale(0.95)';
      ps.pointerEvents = 'auto';
      popup.offsetHeight;
      ps.transition = `opacity ${DUR_OPEN} ease-out, transform ${DUR_OPEN} ${EASE}`;
      ps.opacity = '1';
      ps.transform = 'scale(1)';
    } else {
      // Already open: morph size and reposition; opacity/scale stay at 1
      ps.transition = [
        `left ${DUR_MORPH} ${EASE}`,
        `width ${DUR_MORPH} ${EASE}`,
        `height ${DUR_MORPH} ${EASE}`,
      ].join(', ');
      ps.left = `${left}px`;
      ps.width = `${sz.width}px`;
      ps.height = `${sz.height}px`;
    }
  }

  function closeDropdowns(immediate: boolean): void {
    if (!isOpen || !popup) return;
    isOpen = false;
    currentIdx = -1;
    setActiveTrigger(-1);
    const ps = popup.style;
    if (immediate) {
      ps.transition = 'none';
      ps.display = 'none';
      ps.opacity = '0';
      ps.transform = 'scale(0.95)';
      ps.pointerEvents = 'none';
    } else {
      ps.transition = `opacity ${DUR_CLOSE} ease-in, transform ${DUR_CLOSE} ease-in`;
      ps.opacity = '0';
      ps.transform = 'scale(0.95)';
      ps.pointerEvents = 'none';
      popup.addEventListener('transitionend', () => {
        if (!isOpen) {
          ps.transition = 'none';
          ps.display = 'none';
        }
      }, { once: true });
    }
  }

  if (navRoot && popup) {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', measurePanels);
    } else {
      measurePanels();
    }

    let resizeTimer: number | null = null;
    window.addEventListener('resize', () => {
      if (resizeTimer !== null) clearTimeout(resizeTimer);
      resizeTimer = setTimeout(() => {
        measurePanels();
        if (isOpen && popup) {
          const sz = panelSizes[currentIdx];
          const ps = popup.style;
          ps.transition = 'none';
          ps.left = `${popupLeftFor(currentIdx)}px`;
          ps.width = `${sz.width}px`;
          ps.height = `${sz.height}px`;
        }
      }, 150);
    });

    triggerBtns.forEach((btn, idx) => {
      const li = btn.parentElement!;

      li.addEventListener('mouseenter', () => {
        if (closeTimer !== null) clearTimeout(closeTimer);
        if (openTimer !== null) clearTimeout(openTimer);
        openTimer = setTimeout(() => openDropdown(idx), HOVER_OPEN_DELAY);
      });

      li.addEventListener('mouseleave', () => {
        if (openTimer !== null) clearTimeout(openTimer);
        closeTimer = setTimeout(() => closeDropdowns(false), HOVER_CLOSE_DELAY);
      });

      btn.addEventListener('click', () => {
        if (openTimer !== null) clearTimeout(openTimer);
        if (closeTimer !== null) clearTimeout(closeTimer);
        if (isOpen && currentIdx === idx) {
          closeDropdowns(false);
        } else {
          openDropdown(idx);
        }
      });

      btn.addEventListener('keydown', (e: KeyboardEvent) => {
        if (e.key === 'Escape') {
          // No btn.focus() here: the trigger already has focus. The popup's
          // own keydown handler handles Escape from inside the popup.
          if (isOpen) closeDropdowns(true);
          return;
        }
        if (e.key === 'ArrowDown' || e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          if (isOpen && currentIdx === idx) {
            if (e.key === 'ArrowDown') {
              panelItems(idx)[0]?.focus();
            } else {
              closeDropdowns(true);
            }
          } else {
            openDropdown(idx);
            panelItems(idx)[0]?.focus();
          }
          return;
        }
        if (e.key === 'ArrowUp') {
          e.preventDefault();
          if (!isOpen || currentIdx !== idx) openDropdown(idx);
          const items = panelItems(idx);
          items[items.length - 1]?.focus();
        }
      });
    });

    popup.addEventListener('mouseenter', () => {
      if (closeTimer !== null) clearTimeout(closeTimer);
    });

    popup.addEventListener('mouseleave', () => {
      closeTimer = setTimeout(() => closeDropdowns(false), HOVER_CLOSE_DELAY);
    });

    popup.addEventListener('keydown', (e: KeyboardEvent) => {
      if (currentIdx < 0) return;
      if (e.key === 'Escape') {
        e.preventDefault();
        const trigger = triggerBtns[currentIdx];
        closeDropdowns(true);
        trigger?.focus();
        return;
      }
      const items = panelItems(currentIdx);
      if (items.length === 0) return;
      const activeIdx = items.indexOf(document.activeElement as HTMLElement);
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        items[activeIdx >= 0 ? (activeIdx + 1) % items.length : 0].focus();
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        items[activeIdx > 0 ? activeIdx - 1 : items.length - 1].focus();
      } else if (e.key === 'Home') {
        e.preventDefault();
        items[0].focus();
      } else if (e.key === 'End') {
        e.preventDefault();
        items[items.length - 1].focus();
      } else if (e.key === 'Tab' && e.shiftKey && activeIdx === 0) {
        // The popup sits after the triggers in DOM order, so Shift+Tab from
        // the first item would land on the last trigger — not the one that
        // opened this menu. Redirect back to the active trigger and close.
        e.preventDefault();
        const trigger = triggerBtns[currentIdx];
        closeDropdowns(true);
        trigger?.focus();
      } else if (e.key === 'Tab' && !e.shiftKey && activeIdx === items.length - 1) {
        // Forward Tab from the last item: close the popup and focus the next
        // top-level nav item — dropdown trigger or plain link — so we don't
        // skip plain-link items that sit between dropdowns. If we're at the
        // last top-level item, fall through to default Tab so focus exits
        // the nav to the CTAs.
        const trigger = triggerBtns[currentIdx];
        const triggerPos = topLevelItems.indexOf(trigger);
        const nextItem = triggerPos >= 0 ? topLevelItems[triggerPos + 1] : null;
        if (nextItem) {
          e.preventDefault();
          closeDropdowns(true);
          nextItem.focus();
        }
      }
    });

    // Close when keyboard focus leaves the nav entirely (e.g. Tab past the
    // last popup item). The popup is the last child of navRoot, so a forward
    // Tab from the last item naturally exits the nav.
    navRoot.addEventListener('focusout', (e: FocusEvent) => {
      const next = e.relatedTarget as Node | null;
      if (!next || !navRoot.contains(next)) closeDropdowns(false);
    });

    document.addEventListener('click', (e: MouseEvent) => {
      if (isOpen && navRoot && !navRoot.contains(e.target as Node)) closeDropdowns(false);
    });

    document.addEventListener('keydown', (e: KeyboardEvent) => {
      if (e.key === 'Escape' && isOpen) closeDropdowns(true);
    });
  }

  // ---------- Mobile sheet ----------
  const sheet = document.querySelector<HTMLElement>('[data-nav-sheet]');
  const sheetTrigger = document.querySelector<HTMLElement>('[data-nav-sheet-trigger]');
  const sheetCloseEls = document.querySelectorAll<HTMLElement>('[data-nav-sheet-close]');
  const overlay = document.querySelector<HTMLElement>('[data-nav-sheet-overlay]');
  const navDesktopMql = window.matchMedia('(min-width: 1200px)');

  // Mark every direct child of <body> inert except the sheet, its overlay, and
  // higher-priority overlays (consent banner / consent preferences dialog), so
  // Tab cannot escape the dialog. The sheet uses role="dialog"
  // aria-modal="true", but aria-modal alone does not affect focus order.
  // Track which elements we modified so closing the sheet doesn't clear
  // `inert` from body-level elements that another component owns.
  let bgInerted: Element[] = [];
  function isSheetBypass(el: Element): boolean {
    return (
      el.id === 'segment-consent-manager' ||
      el.classList.contains('consent-dialog-overlay')
    );
  }
  function setBackgroundInert(on: boolean): void {
    if (on) {
      bgInerted = Array.from(document.body.children).filter(
        el =>
          el !== sheet &&
          el !== overlay &&
          !isSheetBypass(el) &&
          !el.hasAttribute('inert'),
      );
      bgInerted.forEach(el => el.setAttribute('inert', ''));
    } else {
      bgInerted.forEach(el => el.removeAttribute('inert'));
      bgInerted = [];
    }
  }

  function openSheet(): void {
    if (!sheet) return;
    sheet.dataset.state = 'open';
    if (overlay) overlay.dataset.state = 'open';
    if (sheetTrigger) sheetTrigger.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
    setBackgroundInert(true);
  }

  function closeSheet(): void {
    if (!sheet) return;
    sheet.dataset.state = 'closed';
    if (overlay) overlay.dataset.state = 'closed';
    if (sheetTrigger) sheetTrigger.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
    setBackgroundInert(false);
    sheetTrigger?.focus();
  }

  if (sheetTrigger) sheetTrigger.addEventListener('click', openSheet);
  if (overlay) overlay.addEventListener('click', closeSheet);
  sheetCloseEls.forEach(el => el.addEventListener('click', closeSheet));

  document.addEventListener('keydown', (e: KeyboardEvent) => {
    if (e.key === 'Escape' && sheet?.dataset.state === 'open') closeSheet();
  });

  // Close the sheet when the viewport crosses into the desktop breakpoint,
  // since the trigger button disappears there and would orphan the open sheet.
  navDesktopMql.addEventListener('change', e => {
    if (e.matches && sheet?.dataset.state === 'open') closeSheet();
  });

  // ---------- Mobile collapsibles ----------
  document.querySelectorAll<HTMLElement>('[data-nav-collapsible]').forEach(item => {
    const trigger = item.querySelector<HTMLElement>('[data-nav-collapsible-trigger]');
    const panel = item.querySelector<HTMLElement>('[data-nav-collapsible-panel]');
    if (!trigger || !panel) return;
    trigger.addEventListener('click', () => {
      const open = item.dataset.open === 'true';
      if (open) {
        item.removeAttribute('data-open');
        panel.dataset.state = 'closed';
        panel.setAttribute('inert', '');
        trigger.setAttribute('aria-expanded', 'false');
      } else {
        item.dataset.open = 'true';
        panel.dataset.state = 'open';
        panel.removeAttribute('inert');
        trigger.setAttribute('aria-expanded', 'true');
      }
    });
  });

  // ---------- Docs nav: Pulumi-logo dropdown ----------
  const logoTrigger = document.querySelector<HTMLElement>('[data-logo-nav-trigger]');
  const logoMenu = document.querySelector<HTMLElement>('[data-logo-nav-menu]');
  if (logoTrigger && logoMenu) {
    const setLogoOpen = (open: boolean): void => {
      logoTrigger.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (open) logoMenu.removeAttribute('hidden');
      else logoMenu.setAttribute('hidden', '');
    };
    logoTrigger.addEventListener('click', e => {
      e.stopPropagation();
      setLogoOpen(logoTrigger.getAttribute('aria-expanded') !== 'true');
    });
    document.addEventListener('click', e => {
      if (logoTrigger.getAttribute('aria-expanded') !== 'true') return;
      const t = e.target as Node;
      if (!logoTrigger.contains(t) && !logoMenu.contains(t)) setLogoOpen(false);
    });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && logoTrigger.getAttribute('aria-expanded') === 'true') {
        setLogoOpen(false);
        logoTrigger.focus();
      }
    });
  }

  // The .is-signed-in class on <html> is set pre-paint by the inline script in
  // head.html — see CSS rules in main.scss. Nothing to do here at hydration.
})();
