function delete_company(){
    Swal.fire({
        icon: 'warning',
        title: 'Warning',
        text:'Are you sure you want to delete this company in your list?',
        showCancelButton: true,
        confirmButtonText: 'Delete',
      }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
          Swal.fire('','','success')
        } else if (result.isDenied) {
          Swal.fire('Changes are not saved', '', 'info')
        }
      })
}