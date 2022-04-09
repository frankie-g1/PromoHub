
//Can only take from specific id
$('#searchbar').keyup(function() {
    var $rows = $('#table tr:not(:first)');


    //takes all values from the searchbar and turn them to lowercase
    //trim values first, than made it lowercase
    //technically, you can just do thid $(this).val()
    var val = $.trim($(this).val()).toLowerCase();

    //filter out rows with elements that pass the test in the function
    $rows.show().filter(function() {
        var text = $(this).text().toLowerCase();

        //indexOf returns the number of index, !~ is like a true/false statement
        return !~text.indexOf(val);
    }).hide();
    //.hide() hides the seected rows
});

$('#creatorbar').keyup(function() {

    var $rows = $('#table tr:not(:first)');


    //takes all values from the searchbar and turn them to lowercase
    //trim values first, than made it lowercase
    //technically, you can just do thid $(this).val()
    var val = $.trim($(this).val()).toLowerCase();


    //filter out rows with elements that pass the test in the function
    $rows.show().filter(function() {
        var text = $(this.cells[0]).text().toLowerCase();
        console.log(text); // this should show up in console, but does not

        //indexOf returns the number of index, !~ is like a true/false statement
        return !~text.indexOf(val);
    }).hide();
    //.hide() hides the seected rows
});

$('#promocodebar').keyup(function() {
    var $rows = $('#table tr:not(:first)');


    //takes all values from the searchbar and turn them to lowercase
    //trim values first, than made it lowercase
    //technically, you can just do thid $(this).val()
    var val = $.trim($(this).val()).toLowerCase();

    //filter out rows with elements that pass the test in the function
    $rows.show().filter(function() {
        var text = $(this.cells[1]).text().toLowerCase();

        //indexOf returns the number of index, !~ is like a true/false statement
        return !~text.indexOf(val);
    }).hide();
    //.hide() hides the seected rows
});

$('#productbar').keyup(function() {
    var $rows = $('#table tr:not(:first)');


    //takes all values from the searchbar and turn them to lowercase
    //trim values first, than made it lowercase
    //technically, you can just do thid $(this).val()
    var val = $.trim($(this).val()).toLowerCase();

    //filter out rows with elements that pass the test in the function
    $rows.show().filter(function() {
        var text = $(this.cells[2]).text().toLowerCase();

        //indexOf returns the number of index, !~ is like a true/false statement
        return !~text.indexOf(val);
    }).hide();
    //.hide() hides the seected rows
});
