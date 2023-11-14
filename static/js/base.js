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