var inputsCEP = $('#nome, #consultaID','#teste');
var validacep = /^[0-11]{8}$/;

function limpa_formulário_cpf(alerta) {
  if (alerta !== undefined) {
    alert(alerta);
  }

  inputsCEP.val('');
}

function get(url) {

  $.get(url, function(data) {

    if (!("erro" in data)) {

      if (Object.prototype.toString.call(data) === '[object Array]') {
        var data = data[0];
      }

      $.each(data, function(nome, info) {
        $('#' + nome).val(nome === 'cpf' ? info.replace(/\D/g, '') : info).attr('info', nome === 'cpf' ? info.replace(/\D/g, '') : info);
      });



    } else {
      limpa_formulário_cep("CEP não encontrado.");
    }

  });
}

// Digitando CEP
$('#cpf').on('blur', function(e) {
  alert("Ok")
  var cpf = $('#cpf').val().replace(/\D/g, '');

  if ("" == "" ) {

    inputsCEP.val('...');
    get('https://api.cpfcnpj.com.br/e6cc0c8ac7fddca7d4a7bb45bcb2a813/1/json/'+ cpf)

  } else {
    limpa_formulário_cpf(cpf == "" ? undefined : "Formato de CEP inválido.");
  }
});
