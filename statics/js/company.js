$(document).ready(
    init
)

function init(){
    console.log('init........')
    load_owner_companies();

    var user_id = $('#user_id').val()
    load_companies_by_user_invited(user_id);

    load_customer_companies(user_id);

    var company_id = $('#company_id').val();
    console.log(company_id)
    if (company_id){
        load_owner_company_data(company_id);
    }

}

//cargas empresas propietarias asociadas a un usuario
function load_owner_companies(){
    var url = 'http://localhost:8000/api/v1/companies/';

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
                item = '<tr>'
                item += '<td> <a href="http://localhost:8000/company/EditOwnerCompany/'+v.id +'">'+v.id+'</a></td>';
                item += '<td>'+v.company_nit +'</td>';
                item += '<td>'+v.company_name +'</td>';
                item += '<td>'+v.commercial_name +'</td>';
                item += '<td>'+v.address +'</td>';
                item += '<td>'+v.phone_number +'</td>';
                item += '<td><a class="remove_owner_company" href="" data-company_id="'+v.id +'">Elimnar</a></td>';
                item += '</tr>'


            })
            $(document).find('#companies-table tbody').html(item);

        },
        error: function(xhr){
            console.log(xhr);
        },
    }); //ajax
}


//Cargar empresas propietarias asociadas a un usuario invitado
function load_companies_by_user_invited(user_id){
    var url = 'http://localhost:8000/api/v1/companies/invited-users/'+ user_id;

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
                item = '<tr>'
                item += '<td> <a href="http://localhost:8000/company/DetailOwnerCompany/'+v.id +'">'+v.id+'</a></td>';
                item += '<td>'+v.company_nit +'</td>';
                item += '<td>'+v.company_name +'</td>';
                item += '<td>'+v.commercial_name +'</td>';
                item += '<td>'+v.address +'</td>';
                item += '<td>'+v.phone_number +'</td>';
                item += '<td><a class="remove_owner_company" href="" data-company_id="'+v.id +'">Elimnar</a></td>';
                item += '</tr>'


            })
            $(document).find('#companies-table tbody').html(item);

        },
        error: function(xhr){
            console.log(xhr);
        },
    }); //ajax
}


//Cargar empresas cliente creadas por un usuario invitado
function load_customer_companies(user_id){
    var url = 'http://localhost:8000/api/v1/companies/customers/'+ user_id;

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
                item += '<td> <a href="http://localhost:8000/company/EditCustomerCompany/'+v.father_company+'/'+v.id +'">'+v.id+'</a></td>';
                item += '<td>'+v.company_nit +'</td>';
                item += '<td>'+v.company_name +'</td>';
                item += '<td>'+v.commercial_name +'</td>';
                item += '<td>'+v.address +'</td>';
                item += '<td>'+v.phone_number +'</td>';
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


//Crear/editar Empresa propietaria
$('#send-company-form').on('click', function(){
//    e.preventDefault();

    var form = $('#company-form').serialize();
    console.log(form)

    var form_data = {
        "company_nit": $('#nit').val(),
        "company_name": $('#nombre_empresa').val(),
        "commercial_name": $('#nombre_comercial').val(),
        "address": $('#direccion').val(),
        "phone_number": $('#telefono').val(),
        "email": $('#correo_electronico').val(),
        "web_site": $('#sitio_web').val(),
        "country": $('#pais').val(),
        "state": $('#estado').val(),
        "city": $('#ciudad').val(),
        "company_type": 1,
        "owner": $('#user_id').val()

    };

    //url para la creacion
    var url = 'http://localhost:8000/api/v1/companies/';
    type = 'POST'

    var company_id = $('#company_id').val();
    if (company_id){
        //url par la actualizacion
        url = 'http://localhost:8000/api/v1/companies/'+company_id;
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


//Remover Empresa propietaria
$('.remove_owner_company').on('click', function(){
    var company_id = $(this).data('company_id')
    console.log(company_id);

     url = 'http://localhost:8000/api/v1/companies/'+company_id;
    $.ajax({
        type: 'DELETE',
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


//obtener detalle de una empresa propietaria
function load_owner_company_data(company_id){
    var url = 'http://localhost:8000/api/v1/companies/'+company_id;
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
            $('#nit').val(data.company_nit)
            $('#nombre_empresa').val(data.company_name)
            $('#nombre_comercial').val(data.commercial_name)
            $('#direccion').val(data.address);
            $('#telefono').val(data.phone_number)
            $('#correo_electronico').val(data.email)
            $('#sitio_web').val(data.web_site)
            $('#pais').val(data.country)
            $('#estado').val(data.state)
            $('#ciudad').val(data.city)

        },
        error: function(xhr){
            console.log(xhr);
        },
    }); //ajax
}


//Crear/editar Empresa cliente
$('#send-customer-company-form').on('click', function(){
//    e.preventDefault();

    var form = $('#company-form').serialize();
    console.log(form)

    var form_data = {
        "company_nit": $('#nit').val(),
        "company_name": $('#nombre_empresa').val(),
        "commercial_name": $('#nombre_comercial').val(),
        "address": $('#direccion').val(),
        "phone_number": $('#telefono').val(),
        "email": $('#correo_electronico').val(),
        "web_site": $('#sitio_web').val(),
        "country": $('#pais').val(),
        "state": $('#estado').val(),
        "city": $('#ciudad').val(),
        "company_type": 2,
        "father_company": $('#owner_company').val()

    };

    //url para la creacion
    var url = 'http://localhost:8000/api/v1/companies/';
    type = 'POST'

    var company_id = $('#company_id').val();
    if (company_id){
        //url par la actualizacion
        url = 'http://localhost:8000/api/v1/companies/'+company_id;
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
