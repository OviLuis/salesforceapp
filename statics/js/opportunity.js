$(document).ready(
    init
)

function init(){
    console.log('init........')
    var customer_company_id = $('#customer_company_id').val()
    load_opportunities_by_company(customer_company_id);

    var contact_id = $('#contact_id').val();
    console.log(contact_id)
    if (contact_id){
        load_contact_data(contact_id);
    }

}


//Crear/editar Oportunidad
$('#send-opportunity-form').on('click', function(){
//    e.preventDefault();

    var form_data = {
        "opportunity_name": $('#opportunity_name').val(),
        "opportunity_value": $('#opportunity_value').val(),
        "status": $('#status').val(),
        "active": "S",
        "id_company": $('#customer_company_id').val(),
        "id_contact": $('#id_contact').val()

    };
    console.log(form_data)

    //url para la creacion
    var url = 'http://localhost:8000/api/v1/opportunities/';
    type = 'POST'

    var opportunity_id = $('#opportunity_id').val();
    if (opportunity_id){
        //url par la actualizacion
        url = 'http://localhost:8000/api/v1/opportunities/'+opportunity_id;
        type = 'PUT'
    }

    $.ajax({
        type: type,
        url: url,
        dataType: "json",
        contentType: 'application/x-www-form-urlencoded; charset=utf-8',
        data: form_data,
        processData: true,
        success: function(data){
            //$(".overlay-example").hide();
            console.log(data.status)


        },
        error: function(xhr){
            console.log(xhr);
            if(xhr.responseJSON){
                var err_msg = ''
                $.each(xhr.responseJSON, function(k,v){
                    err_msg += v[0]+'\n';
                })

                alert(err_msg);
            }
        },
    }); //ajax

})


//Cargar oportunidades para una empresa cliente
function load_opportunities_by_company(customer_company_id){
    var url = 'http://localhost:8000/api/v1/opportunities/customer-company/'+ customer_company_id;

    $.ajax({
        type: "GET",
        url: url,
        dataType: "json",
        contentType: 'application/x-www-form-urlencoded; charset=utf-8',
        processData: true,
        success: function(data){
            //$(".overlay-example").hide();
            var  table = $('#companies-table');
            var item = '';
            $.each(data, function(k, v){
                console.log(v)
                item = '<tr>'
                item += '<td> <a href="http://localhost:8000/company/EditOpportunity/'+v.id_company+'/'+v.id +'">'+v.id+'</a></td>';
                item += '<td>'+v.opportunity_name +'</td>';
                item += '<td>'+v.opportunity_value +'</td>';
                item += '<td>'+v.comp_name +'</td>';
                item += '<td>'+v.contact_name +'</td>';
                item += '<td>'+v.status +'</td>';
                item += '<td><a class="remove_owner_company" href="" data-company_id="'+v.id +'">Elimnar</a></td>';
                item += '</tr>'


            })
            $(document).find('#customer-companies-table tbody').html(item);

        },
        error: function(xhr){
            console.log(xhr);
        },
    }); //ajax
}