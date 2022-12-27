<View> 
   <Header value="Speaker Details" />          
   {$speaker_0_details ?
   <Text name="Speaker 0 Details" 
    value="$speaker_0_details"/> : null} 
   {$speaker_1_details ?
   <Text name="Speaker 1 Details" 
    value="$speaker_1_details"/> : null} 


  <Labels name="labels" toName="audio_url" className="ignore_assertion"> 
    {speaker_0_details ? <Label value="$speaker_0_details.split(",")[0].split(": ")[1]" />  : null} 
    {speaker_1_details ? <Label value="$speaker_1_details.split(",")[0].split(": ")[1]" />  : null}
    <Label value="Noise" />
  </Labels> 
  <AudioPlus name="audio_url" value="$audio_url"/> 
  
  <View visibleWhen="region-selected"> 
    <Header value="Provide Transcription" /> 
  </View> 
  
  <TextArea name="transcribed_json" toName="audio_url" 
            rows="2" editable="true" 
            perRegion="true" required="true" /> 
              
  {reference_raw_transcript ? <Header value="Reference Transcript" /> 
   <Text name="reference_raw_transcript" 
    value="$reference_raw_transcript"/> : null} 
   
</View> 
 
