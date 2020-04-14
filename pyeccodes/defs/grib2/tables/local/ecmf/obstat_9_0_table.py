def load(h):
    return ({'abbr': 'count', 'code': 1, 'title': 'data count'},
            {'abbr': 'obs', 'code': 2, 'title': 'Average of observed values'},
            {'abbr': 'obs_stdv',
             'code': 3,
             'title': 'Standard deviation of observed values'},
            {'abbr': 'fgdep', 'code': 4, 'title': 'Average of first guess departure'},
            {'abbr': 'fgdep_stdv',
             'code': 5,
             'title': 'Standard deviation of first guess departure'},
            {'abbr': 'andep', 'code': 6, 'title': 'Average of analysis departure'},
            {'abbr': 'andep_stdv',
             'code': 7,
             'title': 'Standard deviation of analysis departure'},
            {'abbr': 'obs_error',
             'code': 8,
             'title': 'Average of observation standard error'},
            {'abbr': 'obs_error_stdv',
             'code': 9,
             'title': 'Standard deviation of observation standard error'},
            {'abbr': 'bkg_error',
             'code': 10,
             'title': 'Average of background standard error'},
            {'abbr': 'bkg_error_stdv',
             'code': 11,
             'title': 'Standard deviation of background standard error'},
            {'abbr': 'lr_andep1',
             'code': 12,
             'title': 'Average of low resolution analysis departure update 1'},
            {'abbr': 'lr_andep1_stdv',
             'code': 13,
             'title': 'Standard deviation of low resolution analysis departure update 1'},
            {'abbr': 'hr_fgdep2',
             'code': 14,
             'title': 'Average of high resolution background departure update 2'},
            {'abbr': 'hr_fgdep2_stdv',
             'code': 15,
             'title': 'Standard deviation of high resolution background departure update '
                      '2'},
            {'abbr': 'lr_andep2',
             'code': 16,
             'title': 'Average of low resolution analysis departure update 2'},
            {'abbr': 'lr_andep2_stdv',
             'code': 17,
             'title': 'Standard deviation of low resolution analysis departure update 2'},
            {'abbr': 'bcor', 'code': 18, 'title': 'Average of Bias correction'},
            {'abbr': 'bcor_stdv',
             'code': 19,
             'title': 'Standard deviation of bias correction'},
            {'abbr': 'vbcor',
             'code': 20,
             'title': 'average of Variational bias correction'},
            {'abbr': 'vbcor_stdv',
             'code': 21,
             'title': 'Standard deviation of variational bias correction'},
            {'abbr': 'fgdep_nbcor',
             'code': 22,
             'title': 'Average of background departure without bias correction'},
            {'abbr': 'fgdep_nbcor_stdv',
             'code': 23,
             'title': 'Standard deviation of background departure without bias '
                      'correction'},
            {'abbr': 'windspeed', 'code': 24, 'title': 'Average of wind speed'},
            {'abbr': 'windspeed_stdv',
             'code': 25,
             'title': 'Standard deviation of wind speed'},
            {'abbr': 'norm_andep',
             'code': 26,
             'title': 'Average of normalised analysis fit'},
            {'abbr': 'norm_andep_stdv',
             'code': 27,
             'title': 'Standard deviation of normalised analysis fit'},
            {'abbr': 'norm_fgdep',
             'code': 28,
             'title': 'Average of normalised background fit'},
            {'abbr': 'norm_fgdep_stdv',
             'code': 29,
             'title': 'Standard deviation of normalised background fit'},
            {'abbr': 'fso',
             'code': 30,
             'title': 'Average of forecast sensitivity to observations'},
            {'abbr': 'fso_stdv',
             'code': 31,
             'title': 'stdv of forecast sensitivity to observations'},
            {'abbr': 'norm_obs', 'code': 32, 'title': 'Average of normalised observation'},
            {'abbr': 'norm_obs_stdv',
             'code': 33,
             'title': 'stdv of normalised observation'},
            {'abbr': 'anso',
             'code': 34,
             'title': 'Average of analyse sensitivity to observations'},
            {'abbr': 'anso_stdv',
             'code': 35,
             'title': 'stdv of analyse sensitivity to observations'},
            {'abbr': 'fcst_dep1',
             'code': 40,
             'title': 'Average of forecast departure for step 1'},
            {'abbr': 'fcst_dep1_stdv',
             'code': 41,
             'title': 'Standard deviation of forecast departure for step 1'},
            {'abbr': 'fcst_dep2',
             'code': 42,
             'title': 'Average of forecast departure for step 2'},
            {'abbr': 'fcst_dep2_stdv',
             'code': 43,
             'title': 'Standard deviation of forecast departure for step 2'},
            {'abbr': 'norm_fcst_dep1',
             'code': 44,
             'title': 'Average of normalised forecast departure for step 1'},
            {'abbr': 'norm_fcst_dep1_stdv',
             'code': 45,
             'title': 'Standard deviation of normalised forecast departure for step 1'},
            {'abbr': 'norm_fcst_dep2',
             'code': 46,
             'title': 'Average of normalised forecast departure for step 2'},
            {'abbr': 'norm_fcst_dep2_stdv',
             'code': 47,
             'title': 'Standard deviation of normalised forecast departure for step 2'},
            {'abbr': 'far_rate', 'code': 60, 'title': 'False alarm rate'},
            {'abbr': 'miss_rate', 'code': 62, 'title': 'Miss rate'},
            {'abbr': 'hit_rate', 'code': 64, 'title': 'hit rate'},
            {'abbr': 'corr_nul', 'code': 66, 'title': 'correct nuls'},
            {'abbr': 'est_fg_err',
             'code': 68,
             'title': 'Estimated variance of the first guess error'},
            {'abbr': 'edafgspr', 'code': 70, 'title': 'EDA first guess variance'},
            {'abbr': 'edaanspr', 'code': 72, 'title': 'EDA Analysis variance'})