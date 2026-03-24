window.siteConfig = Object.assign(
  {
    formEndpoint: "",
    formServiceName: "Formspree-compatible endpoint",
    volunteerContactLabel: "Volunteer organizer contact",
    volunteerContactValue: "Configure in assets/js/site.js before publishing live approvals."
  },
  window.siteConfig || {}
);

document.addEventListener("DOMContentLoaded", () => {
  const nav = document.querySelector("[data-nav]");
  const toggle = document.querySelector("[data-menu-toggle]");
  if (nav && toggle) {
    toggle.addEventListener("click", () => {
      const open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(open));
      document.body.classList.toggle("menu-open", open);
    });
  }

  document.querySelectorAll("[data-current-path]").forEach((link) => {
    const target = link.getAttribute("href");
    const current = window.location.pathname.replace(/\/index\.html$/, "/");
    const normalizedTarget = target.replace(/index\.html$/, "");
    if (current.endsWith(normalizedTarget) || current === normalizedTarget) {
      link.setAttribute("aria-current", "page");
    }
  });

  document.querySelectorAll("[data-year]").forEach((node) => {
    node.textContent = new Date().getFullYear();
  });

  document.querySelectorAll("[data-form-endpoint]").forEach((form) => {
    if (window.siteConfig.formEndpoint) {
      form.setAttribute("action", window.siteConfig.formEndpoint);
      form.setAttribute("method", "post");
    }
  });

  document.querySelectorAll("[data-form-status]").forEach((status) => {
    status.textContent = window.siteConfig.formEndpoint
      ? `This form is configured to submit through ${window.siteConfig.formServiceName}.`
      : `No external form endpoint is configured yet. Use the printable approval checklist and direct volunteer follow-up until a handler is added.`;
  });

  document.querySelectorAll("[data-contact-label]").forEach((node) => {
    node.textContent = window.siteConfig.volunteerContactLabel;
  });

  document.querySelectorAll("[data-contact-value]").forEach((node) => {
    node.textContent = window.siteConfig.volunteerContactValue;
  });
});

