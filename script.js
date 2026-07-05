(() => {
  const modal = document.querySelector('.modal');
  const open = document.querySelector('[data-open-modal]');
  const close = document.querySelector('[data-close-modal]');
  if (!modal || !open || !close) return;
  open.addEventListener('click', () => {
    modal.hidden = false;
    close.focus();
  });
  close.addEventListener('click', () => {
    modal.hidden = true;
    open.focus();
  });
  modal.addEventListener('click', (event) => {
    if (event.target === modal) close.click();
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && !modal.hidden) close.click();
  });
})();
