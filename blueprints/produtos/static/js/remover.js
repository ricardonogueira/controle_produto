function remover (id) {

    const resposta = confirm("Deseja realmente excluir este registro?");
    console.log(resposta);

    if (resposta) {
        url = '/produtos/excluir';
        
        const formData = new FormData();
        formData.append('id', id);
        console.log(formData)
        
        fetch(url, {
            "method": "Post",
            "body": formData 
        })
    }
}