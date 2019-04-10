//variable that holds the colorPicker Id element
var color = document.querySelector('#colorPicker');
//variable for the size of the table
var tableSize = document.querySelector('#sizePicker');

//makeGrid functin which when called creates the grids

function makeGrid() {
    var table = document.querySelector('#pixelCanvas');
    var height = document.querySelector('#inputHeight').value;
    var width = document.querySelector('#inputWidth').value;
    //refresh the table with no value each time the makeGrid function is called afresh
    table.innerHTML = '';
    //creates rows using the input height
        for (var r = 0; r < height; r++){
            var row = document.createElement('tr');
            table.appendChild(row)
            /*creates cells using the input width on the form. It is an inner loop of the row loop 
              the number of cells is dependent on the number of rows. If there are 2 rows and 3 cells, 
              the inner loop runs 3 times each time the outer loop runs once(1 outer loop * 3 inner loop times)
              giving one row and three columns for each run*/
            for (var c = 0; c < width; c++){
                var cell = document.createElement('td');
                table.appendChild(cell);
                /*even listener that adds color to cell when you click on the cell
                  the e.target will make the browser listen to only clicks in the cells
                  and not any other place in the DOM*/
                cell.addEventListener('click', function(e){
                    var addColor = colorPicker.value;
                    e.target.style.backgroundColor = addColor;
                });
            }
    }
}
/*When size is submitted by the user, call makeGrid()
  the preventDefault will prevent the submit button from executing or redirecting since we do not actaully
  want it to submit any data*/
tableSize.addEventListener('submit', function(e){
    e.preventDefault();
    makeGrid();
});