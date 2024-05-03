document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('#form-cliente')
  const listaClientes = document.querySelector('#listaClientes')

  form.addEventListener('submit', async (event) => {
    event.preventDefault()
    
    const nome = event.target.elements['nome'].value
    const email = event.target.elements['email'].value
    const rua = event.target.elements['rua'].value
    const bairro = event.target.elements['bairro'].value
    const casa = event.target.elements['casa'].value
    const telefone = event.target.elements['telefone'].value
    const cpf = event.target.elements['cpf'].value
    
    try {
      const response = await axios.post('http://localhost:8000/cliente', {
        id: 1,
        nome: nome,
        email: email,
        rua: rua,
        bairro: bairro,
        numeroCasa: casa,
        numeroTelefone: telefone,
        cpf: cpf
      });

      carregarClientes()
      alert('Cadastrado com sucesso!')
    } catch(e) {
      console.error('Erro ao cadastrar cliente:', e);
      alert('Erro ao cadastrar cliente. Verifique os dados e tente novamente.');
    }
  })

  async function carregarClientes() {
    try {
      const response = await axios.get('http://localhost:8000/cliente')
      const clientes = response.data;

      listaClientes.innerHTML = ''

      clientes.forEach(cliente => {
          const li = document.createElement('li');
          li.textContent = `ID: ${cliente.id}, Nome: ${cliente.nome}, Email: ${cliente.email}, Rua: ${cliente.rua}, Bairro: ${cliente.bairro}, Casa: ${cliente.casa}, Telefone: ${cliente.telefone}, Cpf: ${cliente.cpf}`
          
          const deleteButton = document.createElement('button')
          deleteButton.textContent = 'Deletar';
          deleteButton.addEventListener('click', async () => {
              try {
                  await axios.delete(`http://localhost:8000/cliente/${cliente.id}`)
                  carregarClientes();
                  alert('Cliente deletado com sucesso.');
              } catch (e) {
                  console.error('Erro ao deletar cliente:', e);
                  alert('Erro ao deletar cliente. Tente novamente mais tarde.');
              }
          });

          li.appendChild(deleteButton);
          listaClientes.appendChild(li);
      });

  } catch (e) {
      console.error('Erro ao carregar clientes:', e);
      alert('Erro ao carregar clientes. Tente novamente mais tarde.');
  }
  }

  carregarClientes()
})