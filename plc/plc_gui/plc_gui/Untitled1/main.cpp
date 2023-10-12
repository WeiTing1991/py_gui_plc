///////////////////////////////////////////////////////////////////////////////
// main.cpp
#include "TcPch.h"
#pragma hdrstop

#include "main.h"
#include "Untitled1Version.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif
DEFINE_THIS_FILE()

///////////////////////////////////////////////////////////////////////////////
// Collection of interfaces implemented by module Cmain
BEGIN_INTERFACE_MAP(Cmain)
	INTERFACE_ENTRY_ITCOMOBJECT()
	INTERFACE_ENTRY(IID_ITcADI, ITcADI)
	INTERFACE_ENTRY(IID_ITcWatchSource, ITcWatchSource)
///<AutoGeneratedContent id="InterfaceMap">
///</AutoGeneratedContent>
END_INTERFACE_MAP()

IMPLEMENT_IPERSIST_LIB(Cmain, VID_Untitled1, CID_Untitled1Cmain)
IMPLEMENT_ITCOMOBJECT(Cmain)
IMPLEMENT_ITCOMOBJECT_SETSTATE_LOCKOP2(Cmain)
IMPLEMENT_ITCADI(Cmain)
IMPLEMENT_ITCWATCHSOURCE(Cmain)

///////////////////////////////////////////////////////////////////////////////
// Set parameters of Cmain 
BEGIN_SETOBJPARA_MAP(Cmain)
	SETOBJPARA_DATAAREA_MAP()
///<AutoGeneratedContent id="SetObjectParameterMap">
///</AutoGeneratedContent>
END_SETOBJPARA_MAP()

///////////////////////////////////////////////////////////////////////////////
// Get parameters of Cmain 
BEGIN_GETOBJPARA_MAP(Cmain)
	GETOBJPARA_DATAAREA_MAP()
///<AutoGeneratedContent id="GetObjectParameterMap">
///</AutoGeneratedContent>
END_GETOBJPARA_MAP()

///////////////////////////////////////////////////////////////////////////////
// Get watch entries of Cmain
BEGIN_OBJPARAWATCH_MAP(Cmain)
	OBJPARAWATCH_DATAAREA_MAP()
///<AutoGeneratedContent id="ObjectParameterWatchMap">
///</AutoGeneratedContent>
END_OBJPARAWATCH_MAP()

///////////////////////////////////////////////////////////////////////////////
// Get data area members of Cmain
BEGIN_OBJDATAAREA_MAP(Cmain)
///<AutoGeneratedContent id="ObjectDataAreaMap">
///</AutoGeneratedContent>
END_OBJDATAAREA_MAP()


///////////////////////////////////////////////////////////////////////////////
// Constructor
Cmain::Cmain()
{
///<AutoGeneratedContent id="MemberInitialization">
///</AutoGeneratedContent>
}

///////////////////////////////////////////////////////////////////////////////
// Destructor
Cmain::~Cmain() 
{
}

///////////////////////////////////////////////////////////////////////////////
// State Transitions 
///////////////////////////////////////////////////////////////////////////////
IMPLEMENT_ITCOMOBJECT_SETOBJSTATE_IP_PI(Cmain)

///////////////////////////////////////////////////////////////////////////////
// State transition from PREOP to SAFEOP
//
// Initialize input parameters 
// Allocate memory
HRESULT Cmain::SetObjStatePS(PTComInitDataHdr pInitData)
{
	HRESULT hr = S_OK;
	IMPLEMENT_ITCOMOBJECT_EVALUATE_INITDATA(pInitData);
	return hr;
}

///////////////////////////////////////////////////////////////////////////////
// State transition from SAFEOP to OP
//
// Register with other TwinCAT objects
HRESULT Cmain::SetObjStateSO()
{
	HRESULT hr = S_OK;
	return hr;
}

///////////////////////////////////////////////////////////////////////////////
// State transition from OP to SAFEOP
HRESULT Cmain::SetObjStateOS()
{
	HRESULT hr = S_OK;
	return hr;
}

///////////////////////////////////////////////////////////////////////////////
// State transition from SAFEOP to PREOP
HRESULT Cmain::SetObjStateSP()
{
	HRESULT hr = S_OK;
	return hr;
}