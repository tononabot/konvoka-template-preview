(() => {
  const modal = document.querySelector('.modal');
  const opens = [...document.querySelectorAll('[data-open-modal]')];
  const close = document.querySelector('[data-close-modal]');
  let lastTrigger = null;
  if (!modal || !opens.length || !close) return;

  opens.forEach((open) => {
    open.addEventListener('click', () => {
      lastTrigger = open;
      modal.hidden = false;
      close.focus();
    });
  });

  const closeModal = () => {
    modal.hidden = true;
    if (lastTrigger) lastTrigger.focus();
  };

  close.addEventListener('click', closeModal);
  modal.addEventListener('click', (event) => {
    if (event.target === modal) closeModal();
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && !modal.hidden) closeModal();
  });
})();
