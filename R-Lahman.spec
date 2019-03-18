#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Lahman
Version  : 6.0.0
Release  : 15
URL      : https://cran.r-project.org/src/contrib/Lahman_6.0-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Lahman_6.0-0.tar.gz
Summary  : Sean 'Lahman' Baseball Database
Group    : Development/Tools
License  : GPL-2.0
Requires: R-dplyr
Requires: R-plyr
Requires: R-vcd
BuildRequires : R-dplyr
BuildRequires : R-plyr
BuildRequires : R-vcd
BuildRequires : clr-R-helpers

%description
a set of R data.frames. It uses the data on pitching, hitting and fielding
    performance and other tables from 1871 through 2015, as recorded in the 2016
    version of the database.

%prep
%setup -q -c -n Lahman

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523312120

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523312120
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Lahman
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Lahman
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Lahman
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library Lahman|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Lahman/DESC-temp-change-maintainer.txt
/usr/lib64/R/library/Lahman/DESCRIPTION
/usr/lib64/R/library/Lahman/INDEX
/usr/lib64/R/library/Lahman/Meta/Rd.rds
/usr/lib64/R/library/Lahman/Meta/data.rds
/usr/lib64/R/library/Lahman/Meta/demo.rds
/usr/lib64/R/library/Lahman/Meta/features.rds
/usr/lib64/R/library/Lahman/Meta/hsearch.rds
/usr/lib64/R/library/Lahman/Meta/links.rds
/usr/lib64/R/library/Lahman/Meta/nsInfo.rds
/usr/lib64/R/library/Lahman/Meta/package.rds
/usr/lib64/R/library/Lahman/NAMESPACE
/usr/lib64/R/library/Lahman/NEWS
/usr/lib64/R/library/Lahman/R/Lahman
/usr/lib64/R/library/Lahman/R/Lahman.rdb
/usr/lib64/R/library/Lahman/R/Lahman.rdx
/usr/lib64/R/library/Lahman/data/Rdata.rdb
/usr/lib64/R/library/Lahman/data/Rdata.rds
/usr/lib64/R/library/Lahman/data/Rdata.rdx
/usr/lib64/R/library/Lahman/data/datalist
/usr/lib64/R/library/Lahman/demo/batting-summstats.R
/usr/lib64/R/library/Lahman/demo/lahman-dplyr.R
/usr/lib64/R/library/Lahman/help/AnIndex
/usr/lib64/R/library/Lahman/help/Lahman.rdb
/usr/lib64/R/library/Lahman/help/Lahman.rdx
/usr/lib64/R/library/Lahman/help/aliases.rds
/usr/lib64/R/library/Lahman/help/paths.rds
/usr/lib64/R/library/Lahman/html/00Index.html
/usr/lib64/R/library/Lahman/html/R.css
/usr/lib64/R/library/Lahman/scripts/LahmanData.R
/usr/lib64/R/library/Lahman/scripts/compress-data.R
/usr/lib64/R/library/Lahman/scripts/lahman-compare.R
/usr/lib64/R/library/Lahman/scripts/readLahman.R
