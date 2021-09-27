$(document).ready(
    init
)

function init(){
    console.log('init........')
    var customer_company_id = $('#customer_company_id').val()
    load_opportunities_by_company(customer_company_id);

    var opportunity_id = $('#opportunity_id').val();
    console.log(opportunity_id)
    if (opportunity_id){
        load_opportunity_data(opportunity_id);
    }

}


//Crear/editar Oportunidad
$('#send-opportunity-form').on('click', function(){
//    e.preventDefault();
    var customer_company_id = $('#customer_company_id').val();
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
            if(data){
                alert('Oportunidad creada/modificada con exito');
                window.location = 'http://localhost:8000/company/ListOpportunities/'+customer_company_id
            }


        },
        error: function(xhr){
            console.log(xhr);

            if(xhr.status == 200){
                alert('Oportunidad creada/modificada con exito');
                window.location = 'http://localhost:8000/company/ListOpportunities/'+customer_company_id
            }
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
                item += '</tr>'


            })
            $(document).find('#customer-companies-table tbody').html(item);

        },
        error: function(xhr){
            console.log(xhr);
        },
    }); //ajax
}


//obtener detalle de una oportunidad
function load_opportunity_data(opportunity_id){
    var url = 'http://localhost:8000/api/v1/opportunities/'+opportunity_id;
    console.log('url............')
    console.log(url)
    $.ajax({
        type: "GET",
        url: url,
        dataType: "json",
        contentType: 'application/x-www-form-urlencoded; charset=utf-8',
        processData: true,
        success: function(data){
            //$(".overlay-example").hide();
            console.log(data)
            $('#opportunity_name').val(data.opportunity_name)
            $('#opportunity_value').val(data.opportunity_value)
            $('#id_contact').val(data.id_contact)
            $('#status').val(data.status);



        },
        error: function(xhr){
            console.log(xhr);
        },
    }); //ajax
}


//Remover Oportunidad
$(document).find('#remove_opportunity').click(function(){

    console.log('remove owner company.............')
    var opportunity_id = $(this).data('opportunity_id')
    var customer_company_id = $('#customer_company_id').val();
    console.log(opportunity_id);
    if (confirm("Seguro que desea remover esta empresa")){
        console.log('remove')
        var url = 'http://localhost:8000/api/v1/companies/'+opportunity_id;
        $.ajax({
            type: 'DELETE',
            url: url,
            dataType: "json",
            contentType: 'application/x-www-form-urlencoded; charset=utf-8',
            processData: true,
            success: function(data){
                //$(".overlay-example").hide();
                console.log(data.status)
                if(data.status == 200){
                    alert('Oportunidad eliminada con exito');
                    window.location = 'http://localhost:8000/company/ListOpportunities/'+customer_company_id
                }


            },
            error: function(xhr){
                console.log(xhr);
                if(xhr.status == 200){
                    alert('Oportunidad eliminada con exito');
                    window.location = 'http://localhost:8000/company/ListOpportunities/'+customer_company_id
                }
                if(xhr.responseJSON){
                    var err_msg = ''
                    $.each(xhr.responseJSON, function(k,v){
                        err_msg += v[0]+'\n';
                    })

                    alert(err_msg);
                }
            },
        }); //ajax
    }
    else{
        return false;
    }

})