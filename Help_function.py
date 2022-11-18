#Michel Nzikou @UWA-MinEx CRC Perth, October 2022
####This function  create a help library:
#############################################################################################################
def create_orientation_help(col_list,id,layerobjectName):#(elt1, elt2, elt3):
    #Orientations                                       
    d_params             = ['dip','INCLINATIO','INCLINATN']
    d_help               = 'Dip*: field that contains dip information.'
    dd_params            = ["azimuth2",'azimuth','dip direction','AZIMUTH_TR','STRIKE']
    dd_help              = 'Dip Direction*: field that contains dip direction information.'
    sf_params            = ['feature','ObsType','codedescpt','STRUCTURE_','DESCRIPT','SUB_TYPE','SUBFEATURE']
    sf_help              = 'Feature*: field that contains information on type of structure.'
    bedding_params       = ['Bed','Strata','bedding','beding']
    bedding_help         =  'Bedding flag: text to search for in field defined by sf code to show that this is a bedding measurement.'
    otype_params         = ['dip direction','FeatureCodeDesc', 'strike']
    otype_help           = 'Dip Direction Convention*: flag to determine measurement convention (currently <strike> or <dip direction>).'
    bo_params            = ['structypei', 'NEWBGSVS2', 'deform','Blah','YOUNGING','DESCRIPT','No_col','ATTITUDE']
    bo_help              = 'Dip Diection type*: field that contains type of foliation.'
    btype_params         = ['BEOI','Blah','Group_Suit','-','overturned','over']
    btype_help           = 'Overturned flag: text to search for in field defined by bo code to show that this is an overturned bedding measurement.'
   
   #ids 
    o_params             = ['objectid','unique_id','ID','No_col','GEOGRAPHIC']
    o_help               = 'Polygon ID*: object id.'
    gi_params            = ['gi','geopnt_id','objectid','ID','FIELD_STRU','No_col','STATION_ID']
    gi_help              = 'Point ID*: object id for structures.'
  
  ## faults and folds
    fault_params         = ['Fault','ault','S']
    fault_help           = 'Fault flag: text to search for in field defined by f code to show that this is a fault'
    fdipest_vals_params  = ['gentle','NORTH_EAST','Moderate','Listric','Steep','Vertical','No_col','0','shallow,steep,vertical']   
    dipest_vals_help     = 'Fdipest flag: text to search for in field defined by fdipest to give fault dip estimate in increasing steepness'


    fdip_params          = ['dip','CaptureScale','No_col','fixed']
    fdip_help            = 'Default Dip*: field for numeric fault dip value.'
    fdipdir_params       = ['dip_dir','faultdipdi','DipDirection','No_col','0']
    fdipdir_help         = 'Dip Direction*: field for text fault dip direction value.' 
    ff_params            = ['feature','CATEGORY','codedescpt','Type','DESCRIPTIO','FEATURETYP']
    ff_help              = 'Feature*: field that contains information on type of structure.'
    fdipest_params       = ['dip_est','HWALL_ROSE','faultdipan','Dip','No_col','0']
    fdipest_help         = 'Fdipest*: field for text fault dip estimate value.'
 
  ## stratigraphy   
    c_params             = ['unitname','FM_EQ_D','unit_name','LithDescn1','STRATNAME','SYMBOL','FORMATTED_','LABEL']
    c_help               = 'Formation*: field that contains finer stratigraphic coding.'                                  
    g_params             = ['group_','MAX_PERIOD','sub_provin','Super_Grou','PARENTNAME','SUPERGROUP','No_col','MAX_AGE']
    g_help               =  'Group*: field that contains coarser stratigraphic coding.'
    g2_params            = ['supergroup','supersuite','Super_Grou','MAX_EPOCH','Formation_','GRP','INTERPRETA','MIN_AGE']
    g2_help              = 'Supergroup*: field that contains alternate coarser stratigraphic coding if <g> is blank.'
    ds_params            = ['descriptn','RANK','deposition','Symbol','STRATDESC','DESCRIPT','TEXT_DESCR','LITH_LIST']
    ds_help              = 'Description*: field that contains information about lithology.'
    u_params             = ['code','RCS','nsw_code','RockCatego','MAINUNIT','SYMBOL','ABBREVIATE','MAP_THEME']
    u_help               = 'FM code*: field that contains alternate stratigraphic coding.'
    r1_params            = ['rocktype1','RCS_ORIGIN','class','LithOther','No_col','RANK','LITH_LIST']
    r1_help              = 'Rocktype 1*: field that contains  extra lithology information.'
    r2_params            = ['rocktype2','No_col','igneous_ty','dolerite','TYPE','GENESIS']
    r2_help              = 'Rocktype 1*: field that contains even more lithology information.'
    sill_params          = ['sill','intrusive']
    sill_help            = 'Sill: text to search for in field defined by ds code to show that this is a sill.'
    intrusive_params     = ['granite','IGNEOUS','intrusive','volc','granit','Intrusion']
    intrusive_help       = 'Intrusion: text to search for in field defined by r1 code to show that this is an intrusion.'
    volcanic_params      = ['volcanic','volc','ID']
    volcanic_help        = 'text to search for in field defined by ds code to show that this is an volv=canic (not intrusion).'

    #timing                                     
    min_params           = ['min_age_ma','MIN_TIME_Y','top_end_ag','AgeMin','RELAGE','MINAGE','No_col', 'RM_AGE']
    min_help             = 'Min Age*: field that contains minimum age of unit defined by ccode.'
    max_params           = ['max_age_ma','MAX_TIME_Y','base_start','AgeMax','RELAGE','MAXAGE','No_col','RM_AGE']
    max_help             = 'Max Age*: field that contains maximum age of unit defined by ccode.'
    ################################
    ## geology params
    pluton_dip_help      = 'pluton_dip: default pluton contact dip [45] In degrees (int)'
    pluton_form_help     = 'pluton_form: Possible forms from domes, saucers or pendant. [‘domes’] (str)'
    intrusion_mode_help  = 'intrusion_mode: 1 to exclude all intrusions from basal contacts, [0] to only exclude sills. [0] (int)'
    max_thick_allowd_help= 'max_thickness_allowed: when estimating local formation thickness [10000] in metres. (int)'
    thickness_buffer_help= 'thickness_buffer: How far away to look for next highest unit when calculating formation thickness [5000] In metres. (int)'
    contact_decimate_help= 'contact_decimate: Save every nth contact data point. 0 means save all data. [5] (int)'
    contact_dip_help     = 'contact_dip: Dip to assign to all new basal contact orientations. If -999 then the nearest interpolated dip for that supergroup will be used instead. [-999] In degrees (int)'
    ctct_ori_decimat_help= 'contact_orientation_decimate: Save every nth contact orientation point. 0 means save all data. [5] (int)'
    misorientation_help  = 'misorientation: [30] Maximum misorientation in pole to great circle of bedding between groups to be considered part of same supergroup (int)'
    ################################
    ## Fault params
    fault_decimate_help  = 'fault_decimate: Save every nth fault data point along fault tace. 0 means save all data. [5] (int)'
    fault_dip_help       = 'fault_dip: default fault dip [90] In degrees (int)'
    min_fault_length_hep = 'min_fault_length: Min fault length to be considered. In metres. [5000] In meters. (int)'
    ################################
    ## Struct params
    misorientation_help  = 'misorientation: [30] Maximum misorientation in pole to great circle of bedding between groups to be considered part of same supergroup (int)'
    ori_decimate_help    = 'orientation_decimate: Save every nth orientation data point. 0 means save all data. [0] type int'

    ################################################ Here we are dealing with Structure layer selection
    structure_label   = ['Dip*','Dip Direction*','Feature*','Dip Direction Convention*','Overturned Field*','Point ID*']
    if layerobjectName=='StructButton':
        help_info =[str(d_help)+'\n \n'+str(dd_help)+'\n \n'+str(sf_help)+'\n \n'+str(otype_help)+'\n \n'+str(btype_help)+'\n \n'+str(gi_help)+'\n \n'+str(bedding_help)
        +'\n \n'+str(misorientation_help)+'\n \n'+str(ori_decimate_help)]
        if id==0:
            for idx,col_elt in enumerate(col_list):
                    for col_dir_params in d_params:
                        if col_elt.lower()==col_dir_params.lower():                 
                            col_list.insert(0,col_list.pop(idx))
        elif id==1:
            for idx,col_elt in enumerate(col_list):
                    for col_dir_params in dd_params:
                        if col_elt.lower()==col_dir_params.lower():                          
                            col_list.insert(0,col_list.pop(idx))
        elif id==2:
            for idx,col_elt in enumerate(col_list):
                    for col_dir_params in sf_params:
                        if col_elt.lower()==col_dir_params.lower():                          
                            col_list.insert(0,col_list.pop(idx))
        elif id==4:
            for idx,col_elt in enumerate(col_list):
                    for col_dir_params in bo_params:
                        if col_elt.lower()==col_dir_params.lower():                          
                            col_list.insert(0,col_list.pop(idx))
        elif id==5:
            for idx,col_elt in enumerate(col_list):
                    for col_dir_params in o_params:
                        if col_elt.lower()==col_dir_params.lower():                          
                            col_list.insert(0,col_list.pop(idx))
        else:
                col_list = col_list

    ################################################ Here we are dealing with Fault layer selection
    fault_label       = ['Default Dip*', 'Dip Direction*','Feature*', 'Dip Direction type*', 'fdipest*', 'Point ID*']
    if layerobjectName=='FaultButton':
        help_info =[str(fdip_help)+'\n \n'+str(fdipdir_help)+'\n \n'+str(ff_help)+'\n \n'+str(bo_help)+'\n \n'+str(fdipest_help)+'\n \n'+str(gi_help)
        +'\n \n'+str(fault_help)+'\n \n'+str(dipest_vals_help) +'\n \n'+ str(fault_decimate_help)+'\n \n'+ str(fault_dip_help)+'\n \n'+str(min_fault_length_hep)]
        if id==0:
            for idx,col_elt in enumerate(col_list):
                    for col_dir_params in fdip_params:
                        if col_elt.lower()==col_dir_params.lower():                 
                            col_list.insert(0,col_list.pop(idx))
        elif id==1:
            for idx,col_elt in enumerate(col_list):
                    for col_dir_params in fdipdir_params:
                        if col_elt.lower()==col_dir_params.lower():                          
                            col_list.insert(0,col_list.pop(idx))
        elif id==2:
            for idx,col_elt in enumerate(col_list):
                if col_elt.lower() == 'feature':
                    for col_dir_params in ff_params:
                        if col_elt.lower()==col_dir_params.lower():                         
                            col_list.insert(0,col_list.pop(idx))
                    break
                else:
                    for col_dir_params in ff_params:
                        if col_elt.lower()==col_dir_params.lower():                        
                            col_list.insert(0,col_list.pop(idx))
        elif id==4:
            for idx,col_elt in enumerate(col_list):
                    for col_dir_params in fdipest_params:
                        if col_elt.lower()==col_dir_params.lower():                          
                            col_list.insert(0,col_list.pop(idx))
        elif id==5:
            for idx,col_elt in enumerate(col_list):
                    for col_dir_params in o_params:
                        if col_elt.lower()==col_dir_params.lower():                          
                            col_list.insert(0,col_list.pop(idx))
        else:
                col_list = col_list

    ################################################ Here we are dealing with Geology layer selection
    geol_label       = ['Formation*', 'Group*','Supergroup*', 'Description*', 'Fm code*', 'Rocktype 1*','Rocktype 2*','Polygon ID*','Min Age*','Max Age*']
    if layerobjectName=='GeolButton':
        help_info =[str(c_help)+'\n \n'+str(g_help)+'\n \n'+str(g2_help)+'\n \n'+str(ds_help)+'\n \n'+str(u_help)+'\n \n'+str(r1_help)
        +'\n \n'+str(r2_help)+'\n \n'+str(o_help)+'\n \n'+str(min_help)+'\n \n'+str(max_help)+'\n \n'+str(sill_help)+'\n \n'+str(intrusive_help)
        + '\n \n'+str(pluton_dip_help)+'\n \n'+str(pluton_form_help)+'\n \n'+str(intrusion_mode_help)+'\n \n'+str(max_thick_allowd_help)
         +'\n \n'+str(thickness_buffer_help)+'\n \n'+str(contact_decimate_help)+'\n \n'+str(contact_dip_help)+'\n \n'+str(ctct_ori_decimat_help)
         +'\n \n'+str(misorientation_help)]

        if id==0:
            for idx,col_elt in enumerate(col_list):
                    for col_dir_params in c_params:
                        if col_elt.lower()==col_dir_params.lower():                 
                            col_list.insert(0,col_list.pop(idx))
        elif id==1:
            for idx,col_elt in enumerate(col_list):
                    for col_dir_params in g_params:
                        if col_elt.lower()==col_dir_params.lower():                 
                            col_list.insert(0,col_list.pop(idx))
        elif id==2:
            for idx,col_elt in enumerate(col_list):
                if col_elt.lower() == 'supergroup':
                    for col_dir_params in g2_params:  
                        if col_elt.lower()==col_dir_params.lower():               
                            col_list.insert(0,col_list.pop(idx))
                    break
                else:
                    for col_dir_params in g2_params:  
                        if col_elt.lower()==col_dir_params.lower():               
                            col_list.insert(0,col_list.pop(idx))
        elif id==3:
            for idx,col_elt in enumerate(col_list):
                    for col_dir_params in ds_params:
                        if col_elt.lower()==col_dir_params.lower():                 
                            col_list.insert(0,col_list.pop(idx))
        elif id==4:
            for idx,col_elt in enumerate(col_list):
                    for col_dir_params in u_params:
                        if col_elt.lower()==col_dir_params.lower():                 
                            col_list.insert(0,col_list.pop(idx))
        elif id==5:
            for idx,col_elt in enumerate(col_list):
                    for col_dir_params in r1_params:
                        if col_elt.lower()==col_dir_params.lower():                 
                            col_list.insert(0,col_list.pop(idx))
        elif id==6:
            for idx,col_elt in enumerate(col_list):
                    for col_dir_params in r2_params:
                        if col_elt.lower()==col_dir_params.lower():                 
                            col_list.insert(0,col_list.pop(idx))
        elif id==7:
            for idx,col_elt in enumerate(col_list):
                if col_elt.lower() == 'objectid':
                    for col_dir_params in o_params:
                        if col_elt.lower()==col_dir_params.lower():                          
                            col_list.insert(0,col_list.pop(idx))
                    break
                else:
                    for col_dir_params in o_params:
                       if col_elt.lower()==col_dir_params.lower():                          
                            col_list.insert(0,col_list.pop(idx)) 
        elif id==8:
            for idx,col_elt in enumerate(col_list):
                    for col_dir_params in min_params:
                        if col_elt.lower()==col_dir_params.lower():                          
                            col_list.insert(0,col_list.pop(idx))
        elif id==9:
            for idx,col_elt in enumerate(col_list):
                    for col_dir_params in max_params:
                        if col_elt.lower()==col_dir_params.lower():                          
                            col_list.insert(0,col_list.pop(idx))
        else:
            col_list = col_list
    return col_list , help_info
