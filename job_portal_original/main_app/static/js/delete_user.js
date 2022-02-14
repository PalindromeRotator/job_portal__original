function delete_user(){
    Swal.fire({
        icon: 'warning',
        title: 'Warning',
        text:'Are you sure you want to delete your account permanently? This action cannot be undone.',
        showCancelButton: true,
        confirmButtonText: 'Delete my Account',
      }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
          Swal.fire('Successfully Delete your account', 'We are sorry for what makes you leave our community :(', 'success')
        } else if (result.isDenied) {
          Swal.fire('Changes are not saved', '', 'info')
        }
      })
}