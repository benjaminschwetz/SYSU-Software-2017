'use strict';

// initializing position
$('#right-panel').css({
    top: $('#result-list').offset().top
});

search = (q, type) => realSearch(q, 'paper');
$('#search-edit').attr('placeholder', 'Search for paper...');