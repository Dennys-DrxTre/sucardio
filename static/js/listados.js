var tablaLP;

// DATA DE INVENTARIO
function getDataP() {
	tablaLP = $('#pagos').DataTable({
		responsive: true,
		autoWidth: false,
		destroy: true,
		deferRender: true,
		"language": {
			"sProcessing": "Procesando...",
			"sLengthMenu": "Mostrar _MENU_ registros",
			"sZeroRecords": "No se encontraron resultados",
			"sEmptyTable": "Ningún dato disponible en esta tabla",
			"sInfo": "Mostrando del _START_ al _END_ de un total de _TOTAL_ registros",
			"sInfoEmpty": "Mostrand del 0 al 0 de un total de 0 registros",
			"sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
			"sInfoPostFix": "",
			"sSearch": "Buscar:",
			"sUrl": "",
			"sInfoThousands": ",",
			"sLoadingRecords": "Cargando...",
			"oPaginate": {
				"sFirst": "<span class='fa fa-angle-double-left'></span>",
				"sLast": "<span class='fa fa-angle-double-right'></span>",
				"sNext": "<span class='fa fa-angle-right'></span>",
				"sPrevious": "<span class='fa fa-angle-left'></span>"
			},
			"oAria": {
				"sSortAscending": ": Activar para ordenar la columna de manera ascendente",
				"sSortDescending": ": Activar para ordenar la columna de manera descendente"
			}
		},
		ajax: {
			url: window.location.pathname,
			type: 'POST',
			data: {
				'action': 'listado_de_pago'
			},
			dataSrc: ""
		},
		columns: [{
			"data": "empleado.ci"
		}, {
			"data": "empleado.nombre"
		}, {
			"data": "empleado.apellido"
		}, {
			"data": "asignacion"
		},{
			"data": "descontrar_dias"
		}, {
			"data": "deduccion"
		}, {
			"data": "total_bs"
		}, {
			"data": "total_dolar"
		}, {
			"data": "fecha_pago"
		}, {
			"data": "fecha_pago"
		}],
		columnDefs: [{
			targets: [-1],
			class: 'text-center',
			orderable: false,
			render: function(data, type, row) {

				var buttons = '<a href="#" rel="detalle_nomina" class="btn btn-icon btn-dark edit"><i class="fas fa-file-pdf"></i></a> ';
				return buttons;
			}

		}],
		initComplete: function(settings, json) {

		}
	});
};
$(function() {
	getDataP();

	$('a[rel="btn_open_modal_report"]').on('click', function () {
        $('#modal_report').modal('show');
    });

	$("#pagos tbody").on('click', 'a[rel="detalle_nomina"]', function() {
		var tr = tablaLP.cell($(this).closest('td, li')).index();
		var data = tablaLP.row(tr.row).data();
		
		window.open(`/detalle-de-pago-de-nomina/${data.id}/`)
		
	});

	$(function() {
		$('input[name="date"]').daterangepicker({
		  opens: 'left',
		  "locale": {
				"format": "YYYY-MM-DD HH:mm",
				"separator": " - ",
				"applyLabel": "Aplicar",
				"cancelLabel": "Cancelar",
				"fromLabel": "De",
				"toLabel": "a",
				"customRangeLabel": "Custom",
				"daysOfWeek": [
					"Do",
					"Lu",
					"Ma",
					"Mi",
					"Ju",
					"Vi",
					"Sa"
				],
				"monthNames": [
					"Enero",
					"Febrero",
					"Marzo",
					"Abril",
					"Mayo",
					"Junio",
					"Julio",
					"Agosto",
					"Septiembre",
					"Octubre",
					"Noviembre",
					"Deciembre"
				],
				"firstDay": 1
			}
		}).on('apply.daterangepicker', function(ev, picker) {
			window.open('/reporte-cesta-ticket/'+ picker.startDate.format('YYYY-MM-DD HH:mm') +'/'+ picker.endDate.format('YYYY-MM-DD HH:mm') + '/')
			
		});;
	});
});

