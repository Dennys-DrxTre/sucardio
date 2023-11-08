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

function Solo_Numero(e){
	var keynum = window.event ? window.event.keyCode : e.which;
	if ((keynum == 8) || (keynum == 46))
	return true;
	return /\d/.test(String.fromCharCode(keynum));
}