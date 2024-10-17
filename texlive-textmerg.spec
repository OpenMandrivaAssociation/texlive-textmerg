Name:		texlive-textmerg
Version:	20677
Release:	2
Summary:	Merge text in TeX and LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/textmerg
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textmerg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textmerg.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textmerg.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
