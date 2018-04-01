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
var section = document.getElementsByClassName("dropdown-content");
var z;
var count = 0;
for (z = 0; z < section.length; z++) {
  section[z].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    for (var i = 0; i < section.length; i++) {
      if(section[i].hasClass()){
        count++;
        if(count > 1){
          section[i].removeClass();
        }
      }
    }
  });
}
function predict(file, dataset){
  var receiver = "vincentpaul.012@gmail.com";
              $.getJSON('/', {
              receive: receiver,
              filename: file,
              dataset: JSON.stringify(dataset)
            });
            

            $.ajax ({
              url: "/sendemail/" + receiver + "/" + file + "/" + dataset,
              success: function(data) {
                console.log(data);
                var table = "";
                var tablerow = "";
                var studentname = "";
                var remarks = "";
                var toptable = "";
                var toptablerow = "";
                var inputtable = "";
                var inputtablerow = "";
                var counter = 1;
                inputtable = document.getElementById("inputTable");
                inputtablerow = inputtable.rows;
                table = "<tr><th>Student</th><th>Second Half Grade</th><th>Final Grade</th><th>Remarks</th><th>Financial</th><th>Family</th><th>Relatives</th><th>Health</th><th>Materials</th><th>Parenting</th><th>Study Habit</th></tr>";
                for (x = 0; x < data.predict_finalgrade.length; x++){
                  studentname = inputtablerow[counter].cells[0].firstChild.data;
                  if(data.predict_finalgrade[x] <= "75"){
                    remarks = "FAILED";
                  }
                  else if(data.predict_finalgrade[x] <= "80" && data.predict_finalgrade >= "76"){
                    remarks = "FAILING";
                  }
                  else if(data.predict_finalgrade[x] >= "81"){
                    remarks = "PASSED";
                  }
                  tablerow = tablerow + "<tr>";
                  toptablerow = toptablerow + "<tr>"
                  tablerow = tablerow + "<td>" + studentname + "</td><td>" + data.predict_secondhalf[x] + "</td><td>" + data.predict_finalgrade[x] + "</td><td>" + remarks + "</td>"; 
                  for (y = 0; y < 7; y++){
                        tablerow = tablerow + "<td>"+ data.fuzzy_results[x][y][1] + "</td>";          
                  }
                  tablerow = tablerow + "</tr>"; 
                  counter++;
                }
                table = table + tablerow;
                document.getElementById("resultstable").innerHTML = table;
                toptable = table; 
                document.getElementById("toptable").innerHTML = toptable;  
                var toptentable, rows, switching, rowIndex, rowX, rowY, shouldSwitch;
                toptentable = document.getElementById('toptable');
                switching = true;
                /* Make a loop that will continue until
                no switching has been done: */
                while (switching) {
                  // Start by saying: no switching is done:
                  switching = false;
                  rows = toptentable.rows;
                  /* Loop through all table rows (except the
                  first, which contains table headers): */
                  for (rowIndex = 1; rowIndex < (rows.length - 1); rowIndex++) {
                    // Start by saying there should be no switching:
                    shouldSwitch = false;
                    /* Get the two elements you want to compare,
                    one from current row and one from the next: */
                    rowX = rows[rowIndex].getElementsByTagName("TD")[2];
                    rowY = rows[rowIndex + 1].getElementsByTagName("TD")[2];
                    // Check if the two rows should switch place:
                    if (rowX.innerHTML < rowY.innerHTML) {
                      // I so, mark as a switch and break the loop:
                      shouldSwitch= true;
                      break;
                    }
                  }
                  if (shouldSwitch) {
                    /* If a switch has been marked, make the switch
                    and mark that a switch has been done: */
                    rows[rowIndex].parentNode.insertBefore(rows[rowIndex + 1], rows[rowIndex]);
                    switching = true;
                  }
                }   
              }
            });
}

//predict - faculty
$('#predict').click(function(e){
var file = "";
var dataset = "None";
file = document.getElementById("openFile").files[0].name;
predict(file, dataset);  
});
$('#predictindividual').click(function(e){
var file = "None";
var name = document.getElementById("studName").value;  
var grade = document.getElementById("grade").value;         
var famSize = document.getElementById("famSize").value; 
var parentStatus = document.getElementById("parentStatus").value; 
var mEdu = document.getElementById("mEdu").value; 
var fEdu = document.getElementById("fEdu").value; 
var mJob = document.getElementById("mJob").value; 
var fJob = document.getElementById("fJob").value; 
var failures = document.getElementById("failures").value; 
var famSup = document.getElementById("famSup").value; 
var activities = document.getElementById("activities").value; 
var internet = document.getElementById("internet").value; 
var health = document.getElementById("health").value; 
var absences = document.getElementById("absences").value; 
var g1 = document.getElementById("g1").value; 
var dataset = [name, grade, famSize, parentStatus, mEdu, fEdu, mJob, fJob, failures, famSup, activities, internet, health, absences, g1];
predict(file, dataset);
opencsv(file,dataset);  
});
function predictadmin(file, dataset){
  console.log(dataset);

  var receiver = "vincentpaul.012@gmail.com";        
            $.getJSON('/', {
              receive: receiver,
              filename: file,
              dataset: dataset
            });
            

            $.ajax ({
              url: "/sendemail/" + receiver + "/" + file + "/" + dataset,
              success: function(data) {
                console.log(data);
                var table = "";
                var tablerow = "";
                var number = "";
                var remarks = "";
                var failedCounter = 0;
                var failingCounter = 0;
                var toptable = "";
                var toptablerow = "";
                var passedCounter = 0;
                var inputtable = "";
                var inputtablerow = "";
                var counter = 1;
                inputtable = document.getElementById("inputTable");
                inputtablerow = inputtable.rows;
                table = "<tr><th>Student</th><th>Second Half Grade</th><th>Final Grade</th><th>Remarks</th><th>Financial</th><th>Family</th><th>Relatives</th><th>Health</th><th>Materials</th><th>Parenting</th><th>Study Habit</th></tr>";
                for (x = 0; x < data.predict_finalgrade.length; x++){
                  studentname = inputtablerow[counter].cells[0].firstChild.data;
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
                  tablerow = tablerow + "<td>" + studentname + "</td><td>" + data.predict_secondhalf[x] + "</td><td>" + data.predict_finalgrade[x] + "</td><td>" + remarks + "</td>"; 
                  for (y = 0; y < 7; y++){
                        tablerow = tablerow + "<td>"+ data.fuzzy_results[x][y][1] + "</td>"            
                  }
                  tablerow = tablerow + "</tr>"; 
                }
                table = table + tablerow;
                document.getElementById("resultstable").innerHTML = table;
                toptable = table; 
                document.getElementById("toptable").innerHTML = toptable;  
                var toptentable, rows, switching, rowIndex, rowX, rowY, shouldSwitch;
                toptentable = document.getElementById('toptable');
                switching = true;
                /* Make a loop that will continue until
                no switching has been done: */
                while (switching) {
                  // Start by saying: no switching is done:
                  switching = false;
                  rows = toptentable.rows;
                  /* Loop through all table rows (except the
                  first, which contains table headers): */
                  for (rowIndex = 1; rowIndex < (rows.length - 1); rowIndex++) {
                    // Start by saying there should be no switching:
                    shouldSwitch = false;
                    /* Get the two elements you want to compare,
                    one from current row and one from the next: */
                    rowX = rows[rowIndex].getElementsByTagName("TD")[2];
                    rowY = rows[rowIndex + 1].getElementsByTagName("TD")[2];
                    // Check if the two rows should switch place:
                    if (rowX.innerHTML < rowY.innerHTML) {
                      // I so, mark as a switch and break the loop:
                      shouldSwitch= true;
                      break;
                    }
                  }
                  if (shouldSwitch) {
                    /* If a switch has been marked, make the switch
                    and mark that a switch has been done: */
                    rows[rowIndex].parentNode.insertBefore(rows[rowIndex + 1], rows[rowIndex]);
                    switching = true;
                  }
                }                   
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
}

//predict - admin
$('#predictadmin').click(function(e){
var file = "";
var dataset = "None";
file = document.getElementById("openFile").files[0].name;
predict(file, dataset);  
});
$('#predictindividualadmin').click(function(e){
var file = "None";
var name = document.getElementById("studName").value;  
var grade = document.getElementById("grade").value;         
var famSize = document.getElementById("famSize").value; 
var parentStatus = document.getElementById("parentStatus").value; 
var mEdu = document.getElementById("mEdu").value; 
var fEdu = document.getElementById("fEdu").value; 
var mJob = document.getElementById("mJob").value; 
var fJob = document.getElementById("fJob").value; 
var failures = document.getElementById("failures").value; 
var famSup = document.getElementById("famSup").value; 
var activities = document.getElementById("activities").value; 
var internet = document.getElementById("internet").value; 
var health = document.getElementById("health").value; 
var absences = document.getElementById("absences").value; 
var g1 = document.getElementById("g1").value; 
var dataset = [name, grade, famSize, parentStatus, mEdu, fEdu, mJob, fJob, failures, famSup, activities, internet, health, absences, g1];
predict(file, dataset);
opencsv(file,dataset);  
});
function opencsv(file, dataset){
  var theFile = file;
 if(file == "None"){
   var table =  document.getElementById("inputTable");
   var tablerow = "";
   table = "<tr><th>Student Name</th><th>Grade</th><th>famSize</th><th>parentStatus</th><th>mEdu</th><th>fEdu</th><th>mJob</th><th>fJob</th><th>failures</th><th>famSup</th><th>activities</th><th>internet</th><th>health</th><th>absences</th><th>g1</th></tr>";
   for(var x = 0; x < dataset.length; x++){
    tablerow = tablerow + "<td>" + dataset[x] + "</td>";
   }
   table = table + "<tr>" + tablerow + "</tr>";
   document.getElementById("inputTable").innerHTML = table;
 }
 else{
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
}
//Input CSV file
$('#openFile').change(function(e){
var fileSize = 0;
   document.getElementById("inputTable").innerHTML = "";
   var file = document.getElementById("openFile").files[0];
   opencsv(file);
});
$('#openFileadmin').change(function(e){
var fileSize = 0;
   document.getElementById("inputTable").innerHTML = "";
   var file = document.getElementById("openFile").files[0];
   opencsv(file);
});
$('#clear').click(function(e){
  document.getElementById("openFile").value = "";
  document.getElementById("inputTable").innerHTML = "";
});
$('#clearindividual').click(function(e){
  document.getElementById("studName").value = "";  
  document.getElementById("grade").value = "";         
  document.getElementById("famSize").value = ""; 
  document.getElementById("parentStatus").value = ""; 
  document.getElementById("mEdu").value = ""; 
  document.getElementById("fEdu").value = ""; 
  document.getElementById("mJob").value = ""; 
  document.getElementById("fJob").value = ""; 
  document.getElementById("failures").value = ""; 
  document.getElementById("famSup").value = ""; 
  document.getElementById("activities").value = ""; 
  document.getElementById("health").value = ""; 
  document.getElementById("internet").value = ""; 
  document.getElementById("health").value = ""; 
  document.getElementById("absences").value = ""; 
  document.getElementById("g1").value = ""; 
});




