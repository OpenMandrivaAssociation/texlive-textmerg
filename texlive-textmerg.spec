# revision 20677
# category Package
# catalog-ctan /macros/latex/contrib/textmerg
# catalog-date 2010-12-01 15:56:49 +0100
# catalog-license pd
# catalog-version 2.01
Name:		texlive-textmerg
Version:	2.01
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Useful, for example, in mail merge.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
