document.addEventListener("rendered", function () {
    const billingPeriod = document.getElementById("billing-period") as HTMLInputElement;
    if (billingPeriod) {
        billingPeriod.addEventListener("change", function (ev) {
            const checked = (ev.target as HTMLInputElement).checked;
            document.querySelectorAll<HTMLElement>(".billing-price-monthly").forEach(p => {
                p.style.display = checked ? "none" : "";
            });
            document.querySelectorAll<HTMLElement>(".billing-price-annually").forEach(p => {
                p.style.display = checked ? "" : "none";
            });
        });
    }
});
