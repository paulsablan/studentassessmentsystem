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
var dataset = [name, grade, famSize, parentStatus, mEdu, fEdu, mJob, fJob, failures, famSup, activities, internet, health, absences, grade];
for(i=0;i<dataset.length;i++)
	dataset[i] = convertIndividual(dataset[i],i);
predict(file, dataset);
dataset = dataset.splice(0,14);
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
predictadmin(file, dataset);
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
var dataset = [name, grade, famSize, parentStatus, mEdu, fEdu, mJob, fJob, failures, famSup, activities, internet, health, absences, grade];
for(i=0;i<dataset.length;i++)
	dataset[i] = convertIndividual(dataset[i],i);
predictadmin(file, dataset);
dataset = dataset.splice(0,14);
opencsv(file,dataset);
});
function convertIndividual(value,i)
{
	if(i == 3)
	{
		if(value >= 3)
			return 1;
		else
			return 2;
	}
	else if(i == 3)
	{
    var strval = value.toUpperCase();
		if(strval.includes("TOGETHER"))
			return 1;
		else
			return 2;
	}
	else if(i == 6 || i == 7)
	{
    var strval = value.toUpperCase();
		if(strval.includes("NONE") || value==1)
			return 1;
		else  if(strval.includes("TEACHER") || strval.includes("EDUCATION") || value==2)
			return 2;
		else  if(strval.includes("HEALTH") || strval.includes("DOCTOR") || value==3)
			return 3;
		else  if(strval.includes("SERVICE") || value==4)
			return 4;
		else
			2;
	}
	else if(i == 4 || i == 5)
	{
    var strval = value.toUpperCase();
		if(strval.includes("NONE") || value==0)
			return 0;
		else if(strval.includes("NURSERY") || value==1)
			return 1;
		else  if(strval.includes("PRIMARY") || strval.includes("ELEMENTARY") || value==2)
			return 2;
		else  if(strval.includes("SECONDARY") || strval.includes("HIGH SCHOOL") || strval.includes("HS") || value==3)
			return 3;
		else  if(strval.includes("TERTIARY") || strval.includes("COLLEGE") || value==4)
			return 4;
		else
			2;
	}
	else if(i == 8)
	{
		if(value >= 3)
			return value;
		else
			return 4;
	}
	else if(i == 9 || i == 10 || i == 11)
	{
    var strval = value.toUpperCase();
    if(strval.includes("NO") || strval.includes("NONE") || value==0)
			return 2;
    else if(strval.includes("YES") || strval.includes("HAVE") || value==1)
			return 1;
    else
      return 1;
	}
	else
		return value;

}
function convertValue(value, i){
	if (i == 2)
	{
		if (value == 1)
			return "Less than 3";
		else
			return "More than 3";
	}
	else if (i == 3)
	{
		if (value == 1)
			return "Together";
		else
			return "Apart";
	}
	else if (i == 4 || i == 5)
	{
		if (value == 0)
			return "None";
		else if (value == 1)
			return "Nursery";
		else if (value == 2)
			return "Primary";
		else if (value == 3)
			return "Secondary";
		else if (value == 4)
			return "Tertiary";
	}
	else if (i == 6 || i == 7)
	{
		if (value == 1)
			return "None";
		else if (value == 2)
			return "Teacher";
		else if (value == 3)
			return "Health";
		else if (value == 4)
			return "Service";
	}
	else if (i == 9)
	{
		if (value == 2)
			return "Not Supported";
		else if (value == 1)
			return "Supported";
	}
	else if (i == 10)
	{
		if (value == 2)
			return "No";
		else if (value == 1)
			return "Yes";
	}
	else if (i == 11)
	{
		if (value == 2)
			return "No";
		else if (value == 1)
			return "Yes";
	}
	else
		return value;
}
function interpretValue(value, i){
	if (i == 1)
		return "Midterm Grade";
	else if (i == 2)
		return "Family size";
	else if (i == 3)
		return "Parent Status";
	else if (i == 4)
		return "Mother's Education";
	else if (i == 5)
		return "Father's Education";
	else if (i == 6)
		return "Mother's Job";
	else if (i == 7)
		return "Fathers's Job";
	else if (i == 8)
		return "Number of Failures";
	else if (i == 9)
		return "Family Support";
	else if (i == 10)
		return "Extra-curicular Activiites";
	else if (i == 11)
		return "Internet Connection";
	else if (i == 12)
		return "Heatlh Status";
	else if (i == 13)
		return "Absences";
	else
		return value;
}

function opencsv(file, dataset){
  var theFile = file;
 if(file == "None"){
   var table =  document.getElementById("inputTable");
   var tablerow = "";
   table = "<tr><th>Student Name</th><th>Grade</th><th>Family Size</th><th>Parent Status</th><th>Mother's Education</th><th>Father's Education</th><th>Mohter's Job</th><th>Father's Job</th><th>Failures</th><th>Family Support</th><th>Exra-Curiccular Activities</th><th>Internet Access</th><th>Health Status</th><th>Absences</th></tr>";
   for(var x = 0; x < dataset.length; x++){
		dataset[x] = convertValue(dataset[x],x);
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
	 var lines = content.split("\"");
	 for (var count = 1; count < lines.length; count+=2) {
		 var row = document.createElement("tr");
		 var rowContent = lines[count].split(",");
		 for (var i = 0; i < rowContent.length-1; i++) {
			 if(count!=1)
				rowContent[i] = convertValue(rowContent[i],i);
			else
				rowContent[i] = interpretValue(rowContent[i],i);

			 if (count == 0) {
				var cellElement = document.createElement("th");
			 }
			 else {
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
