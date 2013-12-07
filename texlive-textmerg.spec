# revision 20677
# category Package
# catalog-ctan /macros/latex/contrib/textmerg
# catalog-date 2010-12-01 15:56:49 +0100
# catalog-license pd
# catalog-version 2.01
Name:		texlive-textmerg
Version:	2.01
Release:	5
Summary:	Merge text in TeX and LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/textmerg
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textmerg.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textmerg.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textmerg.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Useful, for example, in mail merge.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/textmerg/textmerg.sty
%doc %{_texmfdistdir}/doc/generic/textmerg/results.dat
%doc %{_texmfdistdir}/doc/generic/textmerg/silly.dat
%doc %{_texmfdistdir}/doc/generic/textmerg/textmerg.pdf
%doc %{_texmfdistdir}/doc/generic/textmerg/textmerg.tex
%doc %{_texmfdistdir}/doc/generic/textmerg/tmexamp1.tex
%doc %{_texmfdistdir}/doc/generic/textmerg/tmexamp2.tex
%doc %{_texmfdistdir}/doc/generic/textmerg/tmexampp.tex
#- source
%doc %{_texmfdistdir}/source/generic/textmerg/textmerg.drv
%doc %{_texmfdistdir}/source/generic/textmerg/textmerg.dtx
%doc %{_texmfdistdir}/source/generic/textmerg/textmerg.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.01-2
+ Revision: 756787
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.01-1
+ Revision: 719718
- texlive-textmerg
- texlive-textmerg
- texlive-textmerg

