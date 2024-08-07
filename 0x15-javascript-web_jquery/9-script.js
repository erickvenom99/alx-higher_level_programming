/*
JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr 
and displays the value of hello from that fetch in the HTML tag DIV#hello.
The translation of “hello” must be displayed in the HTML tag DIV#hello
*/
$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (query) {
    $('#hello').text(query.hello);
})

