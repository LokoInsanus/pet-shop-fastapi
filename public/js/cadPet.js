document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('#form-pet')
  const listaPets = document.querySelector('#listaPets')
  const selectDono = document.querySelector('#dono')

  form.addEventListener('submit', async (event) => {
    event.preventDefault()
    
    const nome = event.target.elements['nome'].value
    const animal = event.target.elements['animal'].value
    const dono = selectDono.value
    const raca = event.target.elements['raca'].value
    const rga = event.target.elements['rga'].value
    
    try {
      const response = await axios.post('http://localhost:8000/pet', {
        id: 1,
        nome: nome,
        animal: animal,
        id_dono: dono,
        raca: raca,
        rga: rga
      })

      carregarPets()
      alert('Cadastrado com sucesso!')
    } catch(e) {
      console.error('Erro ao cadastrar pet:', e)
      alert('Erro ao cadastrar pet. Verifique os dados e tente novamente.')
    }
  })

  async function carregarPets() {
    try {
      const response = await axios.get('http://localhost:8000/pet')
      const pets = response.data

      listaPets.innerHTML = ''

      pets.forEach(pet => {
          const li = document.createElement('li')
          li.textContent = `ID: ${pet.id}, Nome: ${pet.nome}, Animal: ${pet.animal}, Dono: ${pet.dono}, Raça: ${pet.raca}, RGA: ${pet.rga}`
          
          const deleteButton = document.createElement('button')
          deleteButton.textContent = 'Deletar'
          deleteButton.addEventListener('click', async () => {
              try {
                  await axios.delete(`http://localhost:8000/pet/${pet.id}`)
                  carregarPets()
                  alert('Pet deletado com sucesso.')
              } catch (e) {
                  console.error('Erro ao deletar pet:', e)
                  alert('Erro ao deletar pet. Tente novamente mais tarde.')
              }
          })

          li.appendChild(deleteButton)
          listaPets.appendChild(li)
      })

  } catch (e) {
      console.error('Erro ao carregar pets:', e)
      alert('Erro ao carregar pets. Tente novamente mais tarde.')
    }
  }

  async function carregarClientes() {
    try {
      const response = await axios.get('http://localhost:8000/cliente')
      const clientes = response.data

      selectDono.innerHTML = ''

      clientes.forEach(cliente => {
        const option = document.createElement('option')
        option.value = cliente.id
        option.textContent = cliente.nome
        selectDono.appendChild(option)
      })

    } catch (e) {
      console.error('Erro ao carregar clientes:', e)
      alert('Erro ao carregar clientes. Tente novamente mais tarde.')
    }
  }

  carregarPets()
  carregarClientes()
})