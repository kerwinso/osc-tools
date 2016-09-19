var validID = false;

//Checks which server based on the class name
function checkserver(x) {
  if (x.contains("dev")) {
    baseurl = "http://legacy-textbook-dev.cnx.org/content/";
    //alert("Dev found " + baseurl);
  }
  if (x.contains("qa")) {
    baseurl = "http://legacy-textbook-qa.cnx.org/content/";
    //alert("QA found " + baseurl);
  }
  if (x.contains("prod")) {
    baseurl = "http://legacy.cnx.org/content/";
    //alert("Production found " + baseurl);
  }
  if (x.contains("staging1")) {
    baseurl = "http://legacy-staging1.cnx.org/content/";
    //alert("staging1 found " + baseurl);
  }
  if (x.contains("staging2")) {
    baseurl = "http://legacy-staging2.cnx.org/content/";
    //alert("staging2 found " + baseurl);
  }
  if (x.contains("staging3")) {
    baseurl = "http://legacy-staging3.cnx.org/content/";
    //alert("staging3 found " + baseurl);
  }
  if (x.contains("staging4")) {
    baseurl = "http://legacy-staging4.cnx.org/content/";
    //alert("staging4 found " + baseurl);
  }
  if (x.contains("staging5")) {
    baseurl = "http://legacy-staging5.cnx.org/content/";
    //alert("staging5 found " + baseurl);
  }
}

// Check if collectionID is valid and starts with a letter
function enterCID() {
  while (!validID) {
    input = prompt("Enter a collection or module ID");
    colID = input.trim();
    if (colID === null || colID === "" ) { //handles the Cancel button in the Prompt
      emptyID = true;
      break;
    }
    if (colID.length == 5 && !isNaN(colID)) {
      validID = true;
      startswithletter = false;
      emptyID = false;
    }
    else if (colID.length == 8 && colID.indexOf("c") == 0) {
      validID = true;
      startswithletter = true;
      emptyID = false;
    }
    else if (colID.length == 6 && colID.indexOf("m") == 0) {
      validID = true;
      startswithletter = true;
      emptyID = false;
    }
    else {
      alert("Invalid ID format, click OK to try again");
    }
  }
}

function enqueue(x) {
  checkserver(x);
  enterCID();
  if (!emptyID && startswithletter) {
    window.open(baseurl + colID + "/latest/enqueue", "_self");
    validID = false;
  }
  if (!emptyID && !startswithletter) {
    window.open(baseurl + "col" + colID + "/latest/enqueue", "_self");
    validID = false;
  }
}

function latest(x) {
  checkserver(x);
  enterCID();
  if (!emptyID && startswithletter) {
    window.open(baseurl + colID + "/latest/", "_self");
    validID = false;
  }
  if (!emptyID && !startswithletter) {
    window.open(baseurl + "col" + colID + "/latest/", "_self");
    validID = false;
  }
}

function qptool(x) {
  checkserver(x);
  enterCID();
  if (!emptyID && startswithletter) {
    window.open(baseurl + colID + "/latest/query_ptool", "_self");
    validID = false;
  }
  if (!emptyID && !startswithletter) {
    window.open(baseurl + "col" + colID + "/latest/query_ptool", "_self");
    validID = false;
  }
}

function printinfo(x) {
  checkserver(x);
  enterCID();
  if (!emptyID && startswithletter) {
    window.open(baseurl + colID + "/latest/printinfo", "_self");
    validID = false;
  }
  if (!emptyID && !startswithletter) {
    window.open(baseurl + "col" + colID + "/latest/printinfo", "_self");
    validID = false;
  }
}

function source(x) {
  checkserver(x);
  enterCID();
  if (!emptyID && startswithletter) {
    window.open(baseurl + colID + "/latest/source", "_self");
    validID = false;
  }
  if (!emptyID && !startswithletter) {
    window.open(baseurl + "col" + colID + "/latest/source", "_self");
    validID = false;
  }
}

function completezip(x) {
  checkserver(x);
  enterCID();
  if (!emptyID && startswithletter) {
    window.open(baseurl + colID + "/latest/complete", "_self");
    validID = false;
  }
  if (!emptyID && !startswithletter) {
    window.open(baseurl + "col" + colID + "/latest/complete", "_self");
    validID = false;
  }
}

function downloadPDF(x) {
  checkserver(x);
  enterCID();
  if (!emptyID && startswithletter) {
    window.open(baseurl + colID + "/latest/pdf", "_self");
    validID = false;
  }
  if (!emptyID && !startswithletter) {
    window.open(baseurl + "col" + colID + "/latest/pdf", "_self");
    validID = false;
  }
}

function versionhistory(x) {
  checkserver(x);
  enterCID();
  if (!emptyID && startswithletter) {
    window.open(baseurl + colID + "/latest/content_info#cnx_history_header", "_self");
    validID = false;
  }
  if (!emptyID && !startswithletter) {
    window.open(baseurl + "col" + colID + "/latest/content_info#cnx_history_header", "_self");
    validID = false;
  }
}

function printparameters(x) {
  alert ("If you update the parameters, don't forget to add \n\n \t /setState?value=public \n\n to the URL afterwards!");
  checkserver(x);
  enterCID();
  if (!emptyID && startswithletter) {
    window.open(baseurl + colID + "/latest/collection_parameters", "_self");
    validID = false;
  }
  if (!emptyID && !startswithletter) {
    window.open(baseurl + "col" + colID + "/latest/collection_parameters", "_self");
    validID = false;
  }
}
