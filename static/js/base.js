urls_filter_medicos = {
	'AC': '/listado-de-medicos/?estado=AC',
	'DE': '/listado-de-medicos/?estado=DE',
	'all': '/listado-de-medicos/',
}

urls_filter_servicios = {
	'AC': '/listado-de-servicios/?estado=AC',
	'DE': '/listado-de-servicios/?estado=DE',
	'all': '/listado-de-servicios/',
}

function formatRepo(repo) {
    if (repo.loading) {
        return repo.text;
    }

    let option = $(
        '<div class="col text-left shadow-sm">' +
        '<p style="margin-bottom: 0;">' +
        '<b>Nombre:</b> ' + repo.text+ '<br>' +
        '<b>Codigo:</b> ' + repo.id + '<br>' +
        '<b>Disponibilidad:</b> ' + repo.others.stock + '<br>' +
        '</p>' +
        '</div>');

    return option;
}

$(function () {
	document.getElementById('select_filter_list_medicos').addEventListener('change', function() {
		var url = this.value;
		if (url) {
			window.location = urls_filter_medicos[url];
		}
	});
	document.getElementById('select_filter_list_servicios').addEventListener('change', function() {
		var url = this.value;
		if (url) {
			window.location = urls_filter_servicios[url];
		}
	});

});

function Solo_Numero(e){
	var keynum = window.event ? window.event.keyCode : e.which;
	if ((keynum == 8) || (keynum == 46))
	return true;
	return /\d/.test(String.fromCharCode(keynum));
}
  
//Solo texto
function Solo_Texto(e) {
	var code;
	if (!e) var e = window.event;
	if (e.keyCode) code = e.keyCode;
	else if (e.which) code = e.which;
	var character = String.fromCharCode(code);
	var AllowRegex  = /^[\ba-zA-Z\s]$/;
	if (AllowRegex.test(character)) return true;     
	return false; 
}
  //Solo numeros sin puntos 
function Solo_Numero_ci(e){
	var keynum = window.event ? window.event.keyCode : e.which;
	if ((keynum == 8))
	return true;
	return /\d/.test(String.fromCharCode(keynum));
}

let reload_spinner = content = `
	<div class="d-flex justify-content-center m-4" id="id_spinner">
		<div class="spinner-grow" style="width: 3rem; height: 3rem" role="status">
			<span class="sr-only">Loading...</span>
		</div>
	</div>
`

const content_search = document.getElementById('content_search');
let searchValue = document.getElementById('search_general');
let content_count = document.getElementById('content_count_result');
let btn_next_page = document.getElementById('btn_next_page');
let btn_previous_page = document.getElementById('btn_previous_page');
// URL de tu vista
let url = 'http://localhost:8000/search/';
// Número de página
let page_number = 1;

const SearchEngine = async (page) => {
	try {
		content_search.innerHTML = reload_spinner

		const response = await fetch (`${url}?page=${page}&search=${searchValue.value}`, {
			method: "GET",
		});
		const data = await response.json();

		if (data['message'] === 'error') {
			console.log('error');
			return false
		} else if (data['message'] === 'success') {

            content_search.innerHTML = "";

			data['results'].forEach(item =>{
                let content = select_content(item, item['model'])
                content_search.append(content);
            });
			content_count.innerHTML = `${data['total_results']} ${(data['total_results'] > 1) ? 'Resultados': 'Resultado'} de: ${data['query']}`

			page_number = (data['current_page']) ? data['current_page'] : 1;
			if (data['next_page'][0]) {
				btn_next_page.style.display ='block';
			}else{
				btn_next_page.style.display ='none';
			}

			if (data['previous_page'][0]) {
				btn_previous_page.style.display ='block';
			}else{
				btn_previous_page.style.display ='none';
			}

			return data
		}

	} catch (error) {
		console.log(error);
	}
}

searchValue.addEventListener('keyup', () => {
	if (searchValue.value.length > 2) {
		SearchEngine(1);
	} else {
		content_search.innerHTML = "sin resultados";
		content_count.innerHTML = "sin resultados";
		btn_previous_page.style.display ='none';
		btn_next_page.style.display ='none';

	}
});

btn_previous_page.addEventListener('click', function() {
	if (page_number > 1) {
		page_number--;
		SearchEngine(page_number);
	}
});
  
btn_next_page.addEventListener('click', function() {
	page_number++;
	SearchEngine(page_number);
});