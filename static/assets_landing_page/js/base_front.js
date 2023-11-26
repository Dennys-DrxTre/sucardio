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

// document.addEventListener('DOMContentLoaded', (event) => {
// 	let count_notificacion = document.getElementsByClassName('count_notificacion');
// 	let content_notificacion = document.getElementsByClassName('content_notificacion');
	
// 	let reload_spinner = content = `
// 		<div class="d-flex justify-content-center m-4" id="id_spinner">
// 			<div class="spinner-grow" style="width: 3rem; height: 3rem" role="status">
// 				<span class="sr-only">Loading...</span>
// 			</div>
// 		</div>
// 	`
	
// 	const content_html_notificacion = (data) => {
// 		let content = document.createRange().createContextualFragment(`
// 			<li class="nav-item">
// 				<a class="dropdown-item" id="${data.id}" href="${data.url}">${data.titulo}</a>
// 			</li>
// 		`);
// 		return content
// 	};
	
// 	const ShowNotifications = async () => {
// 		try {
// 			content_notificacion.innerHTML = reload_spinner
	
// 			const response = await fetch (`/notificaciones/`, {
// 				method: "GET",
// 			});
// 			const data = await response.json();
// 			if (data['message'] === 'error') {
// 				console.log('error');
// 				return false
// 			} else if (data['message'] === 'success') {
// 				content_notificacion.innerHTML = "";
// 				data['notificaciones'].forEach(item =>{
// 					let content = content_html_notificacion(item);
// 					content_notificacion.append(content);
// 				});
// 				count_notificacion.innerHTML = `${data['count']}`
// 				console.log(content_notificacion.innerHTML);
// 				return data
// 			}
	
// 		} catch (error) {
// 			console.log(error);
// 		}
// 	}
// 	count_notificacion.innerHTML = "100";
// 	console.log(count_notificacion.innerHTML);
// 	ShowNotifications();
// });