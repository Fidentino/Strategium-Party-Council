document.onclick = function(item) {
	item = window.event ? event.srcElement : item.target;
	if (item.classList.contains('quoteHeader') && !item.parentNode.classList.contains('closedQuote')) {
		item.parentNode.classList.add('closedQuote');
	}
	else if (item.classList.contains('quoteHeader') && item.parentNode.classList.contains('closedQuote')) {
		item.parentNode.classList.remove('closedQuote');
	}
}