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
  // children don't intercept clicks meant for the active panel.
  function slideContent(nextIdx: number, prevIdx: number): void {
    const dir = prevIdx >= 0 && prevIdx < nextIdx ? 1 : -1;
    contentPanels.forEach((c, i) => {
      if (i === nextIdx) {
        c.style.transition = 'none';
        c.style.opacity = '0';
        c.style.transform = `translateX(${dir * SLIDE_PX}px)`;
        c.style.pointerEvents = 'auto';
        c.offsetHeight; // reflow
        c.style.transition = `opacity ${DUR_MORPH} ${EASE}, transform ${DUR_MORPH} ${EASE}`;
        c.style.opacity = '1';
        c.style.transform = 'translateX(0)';
      } else if (i === prevIdx) {
        c.style.transition = `opacity ${DUR_MORPH} ${EASE}, transform ${DUR_MORPH} ${EASE}`;
        c.style.opacity = '0';
        c.style.transform = `translateX(${-dir * SLIDE_PX}px)`;
        c.style.pointerEvents = 'none';
      } else {
        c.style.transition = 'none';
        c.style.opacity = '0';
        c.style.transform = 'translateX(0)';
        c.style.pointerEvents = 'none';
      }
    });
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
        closeSheet();
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
          closeDropdowns(true);
          btn.focus();
        }
      });
    });

    popup.addEventListener('mouseenter', () => {
      if (closeTimer !== null) clearTimeout(closeTimer);
    });

    popup.addEventListener('mouseleave', () => {
      closeTimer = setTimeout(() => closeDropdowns(false), HOVER_CLOSE_DELAY);
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

  function openSheet(): void {
    if (!sheet) return;
    sheet.dataset.state = 'open';
    if (overlay) overlay.dataset.state = 'open';
    document.body.style.overflow = 'hidden';
  }

  function closeSheet(): void {
    if (!sheet) return;
    sheet.dataset.state = 'closed';
    if (overlay) overlay.dataset.state = 'closed';
    document.body.style.overflow = '';
  }

  if (sheetTrigger) sheetTrigger.addEventListener('click', openSheet);
  if (overlay) overlay.addEventListener('click', closeSheet);
  sheetCloseEls.forEach(el => el.addEventListener('click', closeSheet));

  document.addEventListener('keydown', (e: KeyboardEvent) => {
    if (e.key === 'Escape' && sheet?.dataset.state === 'open') closeSheet();
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
      } else {
        item.dataset.open = 'true';
        panel.dataset.state = 'open';
      }
    });
  });

  // ---------- Auth-aware sign-in / dashboard toggle ----------
  try {
    const cookies: Record<string, string> = {};
    document.cookie.split(';').forEach(c => {
      const eq = c.indexOf('=');
      if (eq > -1) cookies[c.slice(0, eq).trim()] = c.slice(eq + 1).trim();
    });
    const userCookie = cookies['pulumi_web_user_info'] ?? 'j:{}';
    const userInfo = JSON.parse(decodeURIComponent(userCookie).slice(2));
    if (userInfo?.userId) {
      document.querySelectorAll<HTMLElement>('[data-nav-signin]').forEach(el => {
        el.style.display = 'none';
      });
      document.querySelectorAll<HTMLElement>('[data-nav-dashboard]').forEach(el => {
        el.style.removeProperty('display');
      });
    }
  } catch (e) {}
})();
