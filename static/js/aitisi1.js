$(document).ready(function() {
  $('#kids_number').change(function() {
      var selectedOption = $(this).val();
      var fields = [
          '#firstkidNameContainer', '#firstkidBirthContainer',
          '#secondkidNameContainer', '#secondkidBirthContainer',
          '#thirdkidNameContainer', '#thirdkidBirthContainer',
          '#fourthkidNameContainer', '#fourthkidBirthContainer'
      ];

      fields.forEach(function(field) {
          $(field).removeClass('visible').addClass('hidden');
      });

      if (selectedOption === '1') {
          $('#firstkidNameContainer, #firstkidBirthContainer').removeClass('hidden').addClass('visible');
      } else if (selectedOption === '2') {
          $('#firstkidNameContainer, #firstkidBirthContainer, #secondkidNameContainer, #secondkidBirthContainer').removeClass('hidden').addClass('visible');
      } else if (selectedOption === '3') {
          $('#firstkidNameContainer, #firstkidBirthContainer, #secondkidNameContainer, #secondkidBirthContainer, #thirdkidNameContainer, #thirdkidBirthContainer').removeClass('hidden').addClass('visible');
      } else if (selectedOption === '4') {
          $('#firstkidNameContainer, #firstkidBirthContainer, #secondkidNameContainer, #secondkidBirthContainer, #thirdkidNameContainer, #thirdkidBirthContainer, #fourthkidNameContainer, #fourthkidBirthContainer').removeClass('hidden').addClass('visible');
      }
  });

  var autofillButton = document.getElementById('autofillButton');
  if (autofillButton) {
    autofillButton.addEventListener('click', function() {
      document.getElementById('first_name').value = 'John';
      document.getElementById('last_name').value = 'Doe';
      document.getElementById('firstChoice').value = 'Δημοτικός Βρεφονηπιακός Σταθμός Ελαφακια';
      document.getElementById('secondChoice').value = 'Βρεφονηπιακός Σταθμός Πλαγιαρίου Νότες Στοργής';
      document.getElementById('kid_first_name').value = 'Jane';
      document.getElementById('kid_last_name').value = 'Doe';
      document.getElementById('birth_date').value = '2010-01-01';
      document.getElementById('mother_first_name').value = 'Mary';
      document.getElementById('mother_last_name').value = 'Doe';
      document.getElementById('mother_father_name').value = 'John Senior';
      document.getElementById('mother_adt').value = 'AB123456';
      document.getElementById('family_status').value = 'Πολύτεκνη Οικογένεια';
      document.getElementById('amea').value = 'Ναι';
      document.getElementById('kids_number').value = '1';
      document.getElementById('firstkidName').value = 'Anna';
      document.getElementById('firstkid_birthdate').value = '2012-05-15';
      //document.getElementById('secondkidName').value = 'Bob';
      //document.getElementById('secondkid_birthdate').value = '2014-08-20';
      //document.getElementById('thirdkidName').value = 'Charlie';
      //document.getElementById('thirdkid_birthdate').value = '2016-11-25';
      //document.getElementById('fourthkidName').value = 'Daisy';
      // document.getElementById('fourthkid_birthdate').value = '2018-02-10';
      // document.getElementById('Check_dilosi').checked = true;
    });

    autofillButton.addEventListener('click', function() {
      document.getElementById("first_name").value = "John";
      document.getElementById("last_name").value = "Doe";
      document.getElementById("father_fullname").value = "Michael Doe";
      document.getElementById("mother_fullname").value = "Jane Doe";
      document.getElementById("partner_first_name").value = "Emma";
      document.getElementById("birth_date").value = "1985-08-25";
      document.getElementById("home_address").value = "123 Main St";
      document.getElementById("taxidromiki_thirida").value = "45678";
      document.getElementById("cell_number").value = "1234567890";
      document.getElementById("afm").value = "123456789";
      document.getElementById("email").value = "john.doe@example.com";
      document.getElementById("monimi_egkatastasi").checked = true;
      document.getElementById("gamos_dimoti").checked = true;
      document.getElementById("epanadimotefsi").checked = true;
      document.getElementById("arxiki_dimotikotita").checked = true;
      document.getElementById("luseos_gamou").checked = true;
      document.getElementById("upopsifiotita").checked = true;
      document.getElementById("municipality").value = "Thermi";
      //document.getElementById("Check_dilosi").checked = true;
      document.getElementById("Check_prosopika_dedomena").checked = true;
    });
  }})


// Reusable Preview Modal - Metadimotefsi
$(document).ready(function() {
  $('#previewModal_meradimotefsi').on('show.bs.modal', function (e) {
    var button = $(e.relatedTarget); // Button that triggered the modal
    var entryDir = button.data('entry-dir');
    var pdfFilename = button.data('pdf-filename');
    var pdfDietiKatikia = button.data('pdf-dieti-katikia');
    var pdfDilosiEpanadimotefsi = button.data('pdf-dilosi-epanadimotefsi');

    // Update iframe src
    var iframeSrc = `/pdfs/metadimotefsi_sub/${entryDir}/${pdfFilename}`;
    $('#pdfIframe').attr('src', iframeSrc);

    // Update dieti katikia link
    if (pdfDietiKatikia) {
      var dietiKatikiaSrc = `/pdfs/metadimotefsi_sub/${entryDir}/${pdfDietiKatikia}`;
      $('#dietiKatikiaLink').attr('href', dietiKatikiaSrc);
      $('#dietiKatikiaDiv').show();
    } else {
      $('#dietiKatikiaDiv').hide();
    }

    // Update dilosi epanadimotefsi link
    if (pdfDilosiEpanadimotefsi && pdfDilosiEpanadimotefsi !== "None" && pdfDilosiEpanadimotefsi.trim() !== "") {
      var dilosiEpanadimotefsiSrc = `/pdfs/metadimotefsi_sub/${entryDir}/${pdfDilosiEpanadimotefsi}`;
      $('#dilosiEpanadimotefsiLink').attr('href', dilosiEpanadimotefsiSrc);
      $('#dilosiEpanadimotefsiDiv').show();
    } else {
      $('#dilosiEpanadimotefsiDiv').hide();
    }
  });
});

// Reusable Preview Modal - Aitisi1
$(document).ready(function() {
  $('#previewModal_aitisi1').on('show.bs.modal', function (e) {
    var button = $(e.relatedTarget); // Button that triggered the modal
    var entryDir = button.data('entry-dir');
    var pdfFilename = button.data('pdf-filename');

    // Update iframe src for the single modal
    $(this).find('iframe').attr('src', `/pdfs/aitisi1_sub/${entryDir}/${pdfFilename}`);
  });

  // Clear iframe src when the modal is hidden
  $('#previewModal').on('hidden.bs.modal', function () {
    $(this).find('iframe').attr('src', '');
  });
});


// Reusable Delete Modal 
$(document).ready(function() {
  $('#deleteModal').on('show.bs.modal', function (e) {
    var button = $(e.relatedTarget); // Button that triggered the modal
    var formAction = button.data('form-action');

    // Update form action
    $('#deleteForm').attr('action', formAction);
  });
});


