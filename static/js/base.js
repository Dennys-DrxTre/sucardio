urls_filter_servicios = {
	'AC': '/listado-de-medicos/?estado=AC',
	'DE': '/listado-de-medicos/?estado=DE',
	'all': '/listado-de-medicos/',
}

urls_filter_servicios = {
	'AC': '/listado-de-servicios/?estado=AC',
	'DE': '/listado-de-servicios/?estado=DE',
	'all': '/listado-de-servicios/',
}

$(function () {
	document.getElementById('select_filter_list_servicios').addEventListener('change', function() {
		var url = this.value;
		if (url) {
			window.location = urls_filter_servicios[url];
		}
	});
});