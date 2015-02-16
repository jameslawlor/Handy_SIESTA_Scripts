mkdir perturbed
cp H.psf perturbed/
cp C.psf perturbed/
cp submission_script.sh perturbed/
cp submission_script perturbed/

mkdir pristine
mkdir pristine/mol
cp H.psf pristine/mol
cp submission_script.sh pristine/mol
mkdir pristine/host
cp C.psf pristine/host
cp submission_script.sh pristine/host

mkdir single
mkdir single/mol
mkdir single/mol/ghost
mkdir single/mol/no_ghost

cp C.psf single/mol/ghost
cp H.psf single/mol/ghost
mv single/mol/ghost/C.psf single/mol/ghost/Cghost.psf 
cp submission_script.sh single/mol/ghost
cp C.psf single/mol/no_ghost
cp submission_script.sh single/mol/no_ghost

mkdir single/host
mkdir single/host/ghost
cp C.psf single/host/ghost
cp H.psf single/host/ghost
mv single/host/ghost/H.psf Hghost.psf
cp submission_script.sh single/host/ghost
mkdir single/host/no_ghost
cp C.psf single/host/no_ghost
cp submission_script.sh single/host/no_ghost

