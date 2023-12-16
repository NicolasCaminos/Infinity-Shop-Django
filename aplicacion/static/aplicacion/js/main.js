const openBtn = document.querySelector('#show-dialog')
const closeBtn = document.querySelector('#close-dialog')
const modal = document.querySelector('#dialog')

openBtn && openBtn.addEventListener('click', () => {
  modal.showModal()
})

closeBtn && closeBtn.addEventListener('click', () => {
  modal.close()
})
