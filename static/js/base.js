urls_filter_medicos = {
	'AC': '/listado-de-medicos/?estado=AC',
	'DE': '/listado-de-medicos/?estado=DE',
	'all': '/listado-de-medicos/',
}

$(function () {
	document.getElementById('select_filter_list_medicos').addEventListener('change', function() {
		var url = this.value;
		if (url) {
			window.location = urls_filter_medicos[url];
		}
	});
});