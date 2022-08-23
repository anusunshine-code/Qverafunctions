function g_da_fetch_can_send_visit(clientvisit_id) {
   
   // VERSION HISTORY:
   // 2021-08-11 MAP2 - TFS 137681 Initial version
   // 2021-08-23 FP   - TFS 138890 - Changed sql to use query parameterized.
   // 2021-08-27 MAP2 - TFS 138137 - Moved db validation to separate function.
   // 2022-02-09 MAP2 - ADO 8238 - Debugging changes
   
   qie.debug ("in g_da_fetch_can_send_visit");
   
   var defaultReturnValue = false;
   
   var database = channelCache.getValue('database', 'N/A');
        
   try 
   {
      var sqlString = 
            "select vt.send_to_hie, vt.visittype_id, vt.visittype from dbo.VisitType vt " +            
            " inner join dbo.ClientVisit cv on cv.visittype_id = vt.visittype_id" +
            " where cv.clientvisit_id = :ClientVisitId";
            
      var query = qie.getParameterizedQuery(sqlString);      
      
      // Add paramaters values.
      query.setString('ClientVisitId', clientvisit_id);
      
      var queryResult = query.doQuery(database, true);

      if (queryResult.getRowCount() != 0)
      {
         var opt = queryResult.getNode("send_to_hie");      
         var id = queryResult.getNode("visittype_id");
         var desc = queryResult.getNode("visittype");
                  
         
         qie.debug("Processing request for VisitType = " + desc + "  VisitType_Id = " + id);
         qie.debug ("Visit Type.send_to_hie = " + opt);
         
         if (StringUtils.equalsIgnoreCase(opt, "true"))
         { 
            qie.info("A message CAN be sent for this visit type.");
            return true;
         }         
      
      }         
      
      qie.info("A message can NOT be sent for this visit type.");
      return false;
      
   } 
   catch (e) 
   {
      qie.error ("Error checking visit type.  Returning " + defaultReturnValue);
      return defaultReturnValue;
   }
}
