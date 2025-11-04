document.addEventListener('DOMContentLoaded', function () {
  const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
  popoverTriggerList.forEach(function (el) {
    const popover = new bootstrap.Popover(el, {
      trigger: 'manual'
    });
    el.addEventListener('mouseenter', () => popover.show());
    el.addEventListener('mouseleave', () => popover.hide());
  });
});
