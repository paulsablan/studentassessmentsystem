var dropdown = document.getElementsByClassName("dropdown-btn");
var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
} 
//predict - faculty
$('#predict').click(function(e){
var receiver = "vincentpaul.012@gmail.com";
var file = document.getElementById("openFile").files[0].name;          
            $.getJSON('/', {
              receive: receiver,
              filename: file
            });
            
            e.preventDefault();

            $.ajax ({
              url: "/sendemail/" + receiver + "/" + file,
              success: function(data) {
                console.log(data);
                var table = "";
                var tablerow = "";
                var number = "";
                var remarks = "";
                table = "<tr><th>Student</th><th>Second Half Grade</th><th>Final Grade</th><th>Remarks</th><th>Financial</th><th>Family</th><th>Relatives</th><th>Health</th><th>Materials</th><th>Parenting</th><th>Study Habit</th></tr>";
                for (x = 0; x < 395; x++){
                  number = x+1;
                  if(data.predict_finalgrade[x] <= "75"){
                    remarks = "FAILED";
                  }
                  else if(data.predict_finalgrade[x] <= "80" && data.predict_finalgrade >= "76"){
                    remarks = "FAILING";
                  }
                  else if(data.predict_finalgrade[x] >= "81"){
                    remarks = "PASSED";
                  }
                  tablerow = tablerow + "<tr>"
                  tablerow = tablerow + "<td>Student " + number + "</td><td>" + data.predict_secondhalf[x] + "</td><td>" + data.predict_finalgrade[x] + "</td><td>" + remarks + "</td>"; 
                  for (y = 0; y < 7; y++){
                        tablerow = tablerow + "<td>"+ data.fuzzy_results[x][y][1] + "</td>"            
                  }
                  tablerow = tablerow + "</tr>"; 
                }
                table = table + tablerow;
                document.getElementById("resultstable").innerHTML = table;
              }
            });
});
//predict - admin
$('#predictadmin').click(function(e){
var receiver = "vincentpaul.012@gmail.com";
var file = document.getElementById("openFile").files[0].name;          
            $.getJSON('/', {
              receive: receiver,
              filename: file
            });
            
            e.preventDefault();

            $.ajax ({
              url: "/sendemail/" + receiver + "/" + file,
              success: function(data) {
                console.log(data);
                var table = "";
                var tablerow = "";
                var number = "";
                var remarks = "";
                var failedCounter = 0;
                var failingCounter = 0;
                var passedCounter = 0;
                table = "<tr><th>Student</th><th>Second Half Grade</th><th>Final Grade</th><th>Remarks</th><th>Financial</th><th>Family</th><th>Relatives</th><th>Health</th><th>Materials</th><th>Parenting</th><th>Study Habit</th></tr>";
                for (x = 0; x < 395; x++){
                  number = x+1;
                  if(data.predict_finalgrade[x] <= "75"){
                    remarks = "FAILED";
                    failedCounter++;
                  }
                  else if(data.predict_finalgrade[x] <= "80" && data.predict_finalgrade >= "76"){
                    remarks = "FAILING";
                    failingCounter++;
                  }
                  else if(data.predict_finalgrade[x] >= "81"){
                    remarks = "PASSED";
                    passedCounter++;
                  }
                  tablerow = tablerow + "<tr>"
                  tablerow = tablerow + "<td>Student " + number + "</td><td>" + data.predict_secondhalf[x] + "</td><td>" + data.predict_finalgrade[x] + "</td><td>" + remarks + "</td>"; 
                  for (y = 0; y < 7; y++){
                        tablerow = tablerow + "<td>"+ data.fuzzy_results[x][y][1] + "</td>"            
                  }
                  tablerow = tablerow + "</tr>"; 
                }
                table = table + tablerow;
                document.getElementById("resultstable").innerHTML = table;
                // Learning Percentage
                new Chart(document.getElementById("learningChart"), {
                    type: 'doughnut',

                        data: {
                            datasets: [{
                                data: [ passedCounter, failingCounter, failedCounter],
                                backgroundColor: [ "blue","orange", "red"],
                                label: ["Passing", "Failing", "Failed"],
                            }],
                            labels:["Passing","Failing","Failed"],
                        },
                        options: {
                          pieceLabel: {
                            render: 'percentage',
                            fontColor: ['white', 'white', 'white'],
                            fontSize: 20,
                            overlap: 'true',
                            precision: 2
                         }
                        }

                });
              }
            });
});
//Input CSV file
$('#openFile').change(function(e){
var fileSize = 0;
 var theFile = document.getElementById("openFile").files[0];
 if (theFile) {
 var table = document.getElementById("inputTable");
 var headerLine = "";
 var myReader = new FileReader();
 myReader.onload = function(e) {
 var content = myReader.result;
 var lines = content.split("\r");
 for (var count = 0; count < lines.length; count++) {
 var row = document.createElement("tr");
 var rowContent = lines[count].split(",");
 for (var i = 0; i < rowContent.length; i++) {
 if (count == 0) {
 var cellElement = document.createElement("th");
 } else {
 var cellElement = document.createElement("td");
 }
 var cellContent = document.createTextNode(rowContent[i]);
 cellElement.appendChild(cellContent);
 row.appendChild(cellElement);
 }
 inputTable.appendChild(row);
 }
 }
 myReader.readAsText(theFile);
 }
 return false;
});


