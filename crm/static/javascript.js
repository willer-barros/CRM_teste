document.getElementById('btn-usuarios-ativos').addEventListener('click', function() {
    fetch('{% url "usuarios_ativos" %}')
        .then(response => response.json())
        .then(data => {
            const usuariosAtivosBody = document.getElementById('usuarios-ativos-body');

            // Limpar o conteúdo atual da tabela
            usuariosAtivosBody.innerHTML = '';

            // Iterar sobre os usuários ativos e inserir na tabela
            data.usuarios.forEach(usuario => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${usuario.id}</td>
                    <td>${usuario.nome}</td>
                    <td>${usuario.email}</td>
                `;
                usuariosAtivosBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Erro ao obter usuários ativos:', error);
        });
});
