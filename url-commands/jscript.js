var validID = false;
var valid_domain = false;

//Checks which server based on the class name
function checkserver(x) {
  if (x.contains("custom")) {
    while (!valid_domain) {
    domain = prompt("Enter everything before the `.cnx.org` other than `legacy-` (e.g. 'content01'):")
      //cancel button
      if (domain == null) {
        return;
      }
      else if (domain == "") {
        alert("Nothing inputted, try again");
        continue;
      }
      else if (domain !== "") {
        alert("Your domain is: " + domain + ".cnx.org")
        short_url = "https://legacy-" + domain + ".cnx.org/content/";
        long_url = "https://legacy-" + domain + ".cnx.org/content/col";
        servername = "legacy-" + domain + ".cnx.org";
        webview_url = "https://legacy-" + domain + ".cnx.org/content/";
        gob_url = "https://" + domain + ".cnx.org/a/content-status";
        front_end = "https://" + domain + ".cnx.org";
        valid_domain = true;
      }
      else {
        alert("Please enter a valid domain");
        continue;
      }
    }
  }
  if (x.contains("devb")) {
    short_url = "https://legacy-devb.cnx.org/content/";
    long_url = "https://legacy-devb.cnx.org/content/col";
    servername = "legacy-devb.cnx.org";
    webview_url = "https://devb.cnx.org/content/";
    gob_url = "https://devb.cnx.org/a/content-status/";
    front_end = "https://devb.cnx.org";
  }
  if (x.contains("prod")) {
    short_url = "https://legacy.cnx.org/content/";
    long_url = "https://legacy.cnx.org/content/col";
    servername = "legacy.cnx.org";
    webview_url = "https://cnx.org/content/";
    gob_url = "https://cnx.org/a/content-status/";
    front_end = "https://cnx.org";
  }
  if (x.contains("qa")) {
    short_url = "https://legacy-qa.cnx.org/content/";
    long_url = "https://legacy-qa.cnx.org/content/col";
    servername = "legacy-qa.cnx.org";
    webview_url = "https://qa.cnx.org/content/";
    gob_url = "https://qa.cnx.org/a/content-status/";
    front_end = "https://qa.cnx.org";
  }
  if (x.contains("staging")) {
    short_url = "https://legacy-staging.cnx.org/content/";
    long_url = "https://legacy-staging.cnx.org/content/col";
    servername = "legacy-staging.cnx.org";
    webview_url = "https://staging.cnx.org/content/";
    gob_url = "https://staging.cnx.org/a/content-status/";
    front_end = "https://staging.cnx.org";
  }
}

// Check if collectionID is valid and whether to use baseurl+"col"
function enterCID() {
  while (!validID) {
    input = prompt("Enter a legacy collection or module ID for " + servername + " (" + prompt_fn_name + "):");
    colID = input.trim().toLowerCase();
    if (colID === null || colID === "" ) { //handles the Cancel button in the Prompt
      emptyID = true;
      alert("No ID inputted, click OK to try again")
      continue;
    }
    if (colID.length == 5 && !isNaN(colID)) {
      validID = true;
      emptyID = false;
      baseurl = long_url;
    }
    else if (colID.length == 8 && colID.indexOf("c") == 0) {
      validID = true;
      emptyID = false;
      baseurl = short_url;
    }
    else if (colID.length == 6 && colID.indexOf("m") == 0) {
      validID = true;
      emptyID = false;
      baseurl = short_url;
    }
    else {
      alert("Invalid ID format, click OK to try again");
    }
  }
}

// enter module ID for source function only
function enterMID() {
  while (!validID) {
    input = prompt("Enter a legacy module ID to see source for " + servername + ":");
    mID = input.trim().toLowerCase();
    if (mID === null || mID === "" ) { //handles the Cancel button in the Prompt
      emptyID = true;
      alert("No ID inputted, click OK to try again")
      continue;
    }
    if (mID.length == 6 && mID.indexOf("m") == 0) {
      validID = true;
      emptyID = false;
      baseurl = short_url
    }
    else if (mID.length == 5 && !isNaN(mID)) {
      validID = true;
      emptyID = false;
      baseurl = short_url + "m"
    }
    else {
      alert("Invalid module ID format, click OK to try again");
    }
  }
}

// Link command functions below
function collxml(x) {
  prompt_fn_name = "collection.xml";
  checkserver(x);
  enterCID();
  window.open(baseurl + colID + "/latest/source_create", "_self");
  validID = false;
}

function completezip(x) {
  prompt_fn_name = "complete zip";
  checkserver(x);
  enterCID();
  window.open(baseurl + colID + "/latest/complete", "_self");
  validID = false;
}

function downloadPDF(x) {
  prompt_fn_name = "PDF";
  checkserver(x);
  enterCID();
  window.open(baseurl + colID + "/latest/pdf", "_self");
  validID = false;
}

function downloads(x) {
  prompt_fn_name = "downloads list";
  checkserver(x);
  enterCID();
  window.open(baseurl + colID + "/latest/content_info#cnx_downloads_header", "_self");
  validID = false;
}

function enqueue(x) {
  prompt_fn_name = "enqueue";
  checkserver(x);
  enterCID();
  window.open(baseurl + colID + "/latest/enqueue", "_self");
  validID = false;
}

function frontend(x) {
  checkserver(x);
  window.open(front_end, "_self");
  validID = false;
}

function gob(x) {
  checkserver(x);
  window.open(gob_url, "_self");
  validID = false;
}

function gotoserver(x) {
  checkserver(x);
  if (confirm("Click OK to go to " + servername)) {
    window.open("https://" + servername, "_self");
  }
  else {
    valid_domain = false;
  }
}

function latest(x) {
  prompt_fn_name = "latest";
  checkserver(x);
  enterCID();
  window.open(baseurl + colID + "/latest", "_self");
  validID = false;
}

function lock(x) {
  prompt_fn_name = "lock";
  checkserver(x);
  enterCID();
  lock_url = baseurl + colID + "/latest/setProcessStatus?value=locked"
    lock_confirm = confirm("Status may need a few minutes to update. " +
            "Click OK to proceed in a new window. " +
            "\n\nClose the new window to return to this page. " +
            "You'll need to load the printinfo to check the status again."
           )
    if (lock_confirm) {
      window.open(lock_url, "_blank");
      validID = false;
    } else {
      validID = false;
    }
  }

function metadata(x) {
  prompt_fn_name = "content_info";
  checkserver(x);
  enterCID();
  window.open(baseurl + colID + "/latest/content_info", "_self");
  validID = false;
}

function printinfo(x) {
  prompt_fn_name = "printinfo";
  checkserver(x);
  enterCID();
  window.open(baseurl + colID + "/latest/printinfo", "_self");
  validID = false;
}

function printparameters(x) {
  prompt_fn_name = "print parameters";
  alert ("Warning: Use this to look up a parameter only, NOT to update it!");
  checkserver(x);
  enterCID();
  window.open(baseurl + colID + "/latest/collection_parameters", "_self");
  validID = false;
}

function qptool(x) {
  prompt_fn_name = "query_ptool";
  checkserver(x);
  enterCID();
  window.open(baseurl + colID + "/latest/query_ptool", "_self");
  validID = false;
}

function queue_tool(x) {
  checkserver(x);
  // http://legacy-devb.cnx.org/queue_tool/manage_overview?trigger=Refresh
  window.open("https://" + servername + "/queue_tool/manage_overview?trigger=Refresh", "_self");
  validID = false;
}

// view XML source for modules in Chrome only
function source(x) {
  var browser = navigator.userAgent;
  if (browser.search("Chrome") == -1) {
    alert ("Sorry, this feature only works in the Chrome browser");
  }
  else {
    checkserver(x);
    enterMID();
    if (!emptyID) {
      window.open(baseurl + mID + "/latest/source", "_self");
      validID = false;
    }
  }
}

function unlock(x) {
  prompt_fn_name = "unlock";
  checkserver(x);
  enterCID();
  unlock_url = baseurl + colID + "/latest/setProcessStatus?value=succeeded"
    unlock_confirm = confirm("Status may need a few minutes to update. " +
            "Click OK to proceed in a new window. " +
            "\n\nClose the new window to return to this page. " +
            "You'll need to load the printinfo to check the status again."
           )
    if (unlock_confirm) {
      window.open(unlock_url, "_blank");
      validID = false;
    } else {
      validID = false;
    }
  }

function versionhistory(x) {
  prompt_fn_name = "version history";
  checkserver(x);
  enterCID();
  window.open(baseurl + colID + "/latest/content_info#cnx_history_header", "_self");
  validID = false;
}

function webview(x) {
  prompt_fn_name = "webview";
  checkserver(x);
  enterCID();
  if (baseurl == short_url) {
    window.open(webview_url + colID + "/latest/", "_self");
    validID = false;
  }
  if (baseurl == long_url) {
    window.open(webview_url + "col" + colID + "/latest/", "_self");
    validID = false;
  }
}
