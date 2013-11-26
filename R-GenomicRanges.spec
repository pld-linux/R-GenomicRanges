%define		packname	GenomicRanges

Summary:	Representation and manipulation of genomic intervals
Name:		R-%{packname}
Version:	1.14.3
Release:	1
License:	Artistic 2.0
Group:		Applications/Math
Source0:	http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	c5831b8b65363c18edaafcf9426d455e
URL:		http://www.bioconductor.org/packages/release/bioc/html/GenomicRanges.html
BuildRequires:	R
BuildRequires:	R-BiocGenerics
BuildRequires:	R-IRanges-devel >= 1.17.33
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-BiocGenerics
Requires:	R-IRanges >= 1.17.33
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ability to efficiently store genomic annotations and alignments is
playing a central role when it comes to analyze high-throughput
sequencing data (a.k.a. NGS data). The package defines general purpose
containers for storing genomic intervals as well as more specialized
containers for storing alignments against a reference genome.

%prep
%setup -q -c -n %{packname}

%build
# circular dep on R-Rsamtools
#{_bindir}/R CMD build %{packname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/doc/
%doc %{_libdir}/R/library/%{packname}/html/
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/extdata/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/scripts/
%{_libdir}/R/library/%{packname}/unitTests/
%{_libdir}/R/library/%{packname}/libs/
