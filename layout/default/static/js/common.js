
var xml_http_request;
var ajax_error = 'Ошибка AJAX. Вероятно, вы используете устаревший обозреватель.';

// TODO: сделать поддержку множественных уведомлений
function showMessage(text) {
	$('#alert').html(text);
	$('#alert').show();
	$("#alert").delay(3000).fadeOut(300);
}

// Разблокировать всё, что блокировалось — чтобы доставлять меньше удобств в случае, если что-то отказало
function unlockAll() {
	
}

// Наши обновления пришли, посмотрим, что там
function handleUpdates(updates) {
	notifications = parseInt(updates.notifications)
	if(notifications > 0) {
		notifier = $('#notifier');
		notifier.attr('data-content', notifications);
		$('.notifications-link').popover('show');
	} else {
		$('.notifications-link').popover('hide');
	}
}

// Сервер корректно ответил, обработаем ответ
function handleAPIResponse(result) {
	switch(result.method) {
		default:
			showMessage('Неадекватный ответ сервера');
			unlockAll();
		break;
	}
}

// Сервер ответил, но мы пока не знаем, может, там какая-то плесень
function handleServerResponse() {
	if(xml_http_request.readyState == 4 || xml_http_request.readyState == 'complete') {
		if(xml_http_request.status == 200) {
			result = $.parseJSON(xml_http_request.responseText);
			if(result.result != 'ok') {
				showMessage('Ошибка AJAX: ' + result.message);
				return;
			}

			handleAPIResponse(result);
		} else {
			result = $.parseJSON(xml_http_request.responseText);
			showMessage('Ошибка AJAX <' + xml_http_request.status + '> ' + result.message);
			unlockAll();
		}
	}
}

// Получить объект для осуществления запросов
function getXmlHttpObject() {
	var instance = null;

	if(window.XMLHttpRequest) {
		instance = new XMLHttpRequest();
	} else if(window.ActiveXObject) {
		instance = new ActiveXObject('Microsoft.XMLHTTP');
	} else {
		return false;
	}

	instance.onreadystatechange = handleServerResponse;
	return instance;
}

function checkUpdates() {
	if(!(xml_http_request = getXmlHttpObject())) {
		showMessage(ajax_error);
		return false;
	}

	xml_http_request.open("GET", '/api/check_updates', true);
	xml_http_request.send(null);

	setTimeout(checkUpdates, 60000);
}

// Обновимся и поставим обновлять каждые 60 секунд
checkUpdates();
setTimeout(checkUpdates, 60000);

$('#alert').click(function() {
	$("#alert").hide();
});
