const content_html = (title, description,model, color, url) => {
    let content = document.createRange().createContextualFragment(`
        <li class="list-group-item" id="content_search">
            <div class="d-flex align-items-start">
                <div class="flex-grow-1 me-2">
                    <a href="#" class="">
                        <h6 class="mb-0">${title}</h6>
                    </a>
                    <p class="my-1"><i class="ti ti-folder"></i> ${description}</p>
                    <span class="badge ${color} rounded-pill">${model}</span>
                </div>
                <div class="flex-shrink-0">
                    <a href="${url}" class="avtar avtar-s btn btn-info">
                        <i class="ti ti-eye f-18"></i>
                    </a>
                </div>
            </div>
        </li>
    `);
    return content
}

const select_content = (data, model) => {
    let content = ''
    if (model == 'Usuario') {
        content = content_html(
            `${data.cedula}`,
            `nombre de usuario: ${data.cedula} | nombre: ${data.nombre} | apellido: ${data.apellido}`,
            `${data.model}`,
            `bg-dark`,
            `${data.url}`
        );
    } else if (model == 'Medico') {
        content = content_html(
            `${data.nombre} ${data.apellido}`,
            `cedula: ${data.cedula} | nombre: ${data.nombre} | apellido: ${data.apellido}`,
            `${model}`,
            `bg-success`,
            `${data.url}`
        );
    } else if (model == 'Presupuesto') {
        content = content_html(
            `${data.cliente.cedula}`,
            `ID: ${data.id} | cedula: ${data.cliente.cedula} | nombre: ${data.cliente.nombre} | apellido: ${data.cliente.apellido} | metodo de pago: ${data.metodo_pago}`,
            `${model}`,
            `bg-secondary`,
            `${data.url}`
        );
    } else if (model == 'Cita') {
        content = content_html(
            `Motivo de la cita: ${data.motivo_consulta}`,
            `ID: ${data.cliente.pk}  | nombre: ${data.cliente.nombre} | apellido: ${data.cliente.apellido}`,
            `${model}`,
            `bg-info`,
            `${data.url}`
        );
    } else if (model == 'Anuncio') {
        content = content_html(
            `${data.titulo}`,
            `autor: ${data.autor.cedula} | nombre: ${data.autor.nombre} | apellido: ${data.autor.apellido}`,
            `${model}`,
            `bg-warning`,
            `${data.url}`
        );
    }
    return content;
}