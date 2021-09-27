
$(document).ready(
    init
)

function init(){
    console.log('init........')
    var customer_company_id = $('#customer_company_id').val()
    load_contacts_by_company(customer_company_id);

    var contact_id = $('#contact_id').val();
    console.log(contact_id)
    if (contact_id){
        load_contact_data(contact_id);
    }

}


//Crear/editar contacto
$('#send-contact-form').on('click', function(){
//    e.preventDefault();
    console.log('send-contact-form')
    var customer_company_id = $('#customer_company_id').val()
    var form_data = {
        "first_name": $('#first_name').val(),
        "middle_name": $('#middle_name').val(),
        "last_name": $('#last_name').val(),
        "email": $('#email').val(),
        "phone_number": $('#phone_number').val(),
        "mobile_phone_number": $('#mobile_phone_number').val(),
        "status": "S",
        "id_company": customer_company_id

    };

    //url para la creacion
    var url = 'http://localhost:8000/api/v1/contacts/';
    type = 'POST'

    var contact_id = $('#contact_id').val();
    console.log('contact_id................')
    console.log(contact_id)
    if (contact_id){
        console.log('actualizacion')
        //url par la actualizacion
        url = 'http://localhost:8000/api/v1/contacts/'+contact_id;
        type = 'PUT'
        console.log(url)
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
            console.log('exito')
            console.log(data)
            if(data){
                alert('contacto creado/modificado con exito');
                window.location = 'http://localhost:8000/company/ListContact/'+customer_company_id
            }

        },
        error: function(xhr){
            console.log(xhr);
            if(xhr.status == 200){
                alert('contacto creado/modificado con exito');
                window.location = 'http://localhost:8000/company/ListContact/'+customer_company_id
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


//Cargar contactos para una empresa cliente
function load_contacts_by_company(customer_company_id){
    var url = 'http://localhost:8000/api/v1/contacts/customer-company/'+ customer_company_id;

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
                item += '<tr>'
                item += '<td> <a href="http://localhost:8000/company/EditContact/'+v.id_company+'/'+v.id +'">'+v.id+'</a></td>';
                item += '<td>'+v.first_name +'</td>';
                item += '<td>'+v.last_name +'</td>';
                item += '<td>'+v.email +'</td>';
                item += '<td>'+v.phone_number +'</td>';
                item += '<td>'+v.mobile_phone_number +'</td>';
                item += '</tr>'


            })
            $(document).find('#customer-companies-table tbody').html(item);

        },
        error: function(xhr){
            console.log(xhr);
        },
    }); //ajax
}


//obtener detalle de un CONTACTO
function load_contact_data(contact_id){
    var url = 'http://localhost:8000/api/v1/contacts/'+contact_id;
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
            $('#first_name').val(data.first_name)
            $('#middle_name').val(data.middle_name)
            $('#last_name').val(data.last_name)
            $('#email').val(data.email);
            $('#phone_number').val(data.phone_number)
            $('#mobile_phone_number').val(data.mobile_phone_number)


        },
        error: function(xhr){
            console.log(xhr);
        },
    }); //ajax
}


//Remover contacto
$(document).find('#remove_contact').click(function(){

    console.log('remove owner company.............')
    var contact_id = $(this).data('contact_id')
    var customer_company_id = $('#customer_company_id').val()
    console.log(contact_id);
    if (confirm("Seguro que desea remover este contacto")){
        console.log('remove')
        var url = 'http://localhost:8000/api/v1/contacts/'+contact_id;
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
                    alert('Contacto eliminado con exito');
                    window.location = 'http://localhost:8000/company/ListContact/'+customer_company_id
                }


            },
            error: function(xhr){
                console.log(xhr);
                if(xhr.status == 200){
                    alert('Contacto eliminado con exito');
                    window.location = 'http://localhost:8000/company/ListContact/'+customer_company_id
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