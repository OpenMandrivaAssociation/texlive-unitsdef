%global tl_name unitsdef
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Typesetting units in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/unitsdef
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unitsdef.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unitsdef.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unitsdef.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Many packages for typesetting units have been written for use in
LaTeX2e. Some define macros to typeset a lot of units but do not suit to
the actual font settings, some make the characters needed available but
do not predefine any unit. This package tries to comply with both
requirements. It predefines common units, defines an easy to use
interface to define new units and changes the output concerning to the
surrounding font settings.

