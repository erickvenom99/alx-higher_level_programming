/*
document.querySelector('header').style.color = '#FF0000';o.
*/
$(function() {
    const $list = $('.my_list');
  
    $('#add_item').click(() => $list.append('<li>Item</li>'));
    $('#remove_item').click(() => $list.children().last().remove());
    $('#clear_list').click(() => $list.empty());
  });
