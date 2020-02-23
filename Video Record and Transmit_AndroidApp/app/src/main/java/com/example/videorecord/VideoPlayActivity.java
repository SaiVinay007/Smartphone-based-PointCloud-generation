package com.example.videorecord;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import android.Manifest;
import android.annotation.SuppressLint;
import android.app.Activity;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.Environment;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.VideoView;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.URI;
import java.net.UnknownHostException;

public class VideoPlayActivity extends AppCompatActivity {

    private VideoView mVideoView;
    private static final String TAG = "VideoPlayActivity";
    public TextView textView;

    public File file;
    public Uri videoUri;


    // Storage Permissions
    private static final int REQUEST_EXTERNAL_STORAGE = 1;
    private static String[] PERMISSIONS_STORAGE = {
            Manifest.permission.READ_EXTERNAL_STORAGE,
            Manifest.permission.WRITE_EXTERNAL_STORAGE
    };
    

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_video_play);
        mVideoView = findViewById(R.id.videoView);
        textView = findViewById(R.id.textview);

        videoUri = Uri.parse(getIntent().getExtras().getString("videoUri"));

        mVideoView.setVideoURI(videoUri);
        mVideoView.start();

        textView.setText(videoUri.toString());

        verifyStoragePermissions(this);

        final Button clicable1 = (Button) findViewById(R.id.button1);
        clicable1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                send sendfile = new send();
//                message = inputtext.getText().toString();
                Log.d(TAG, "onClick: ============================================");
                sendfile.execute();
                if(sendfile.getStatus() == AsyncTask.Status.FINISHED) {
                    // My AsyncTask is done and onPostExecute was called
                    textView.setText("Sent");
                }
            }
        });

        final Button clicable2 = (Button) findViewById(R.id.button2);
        clicable2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                recieve recievefile = new recieve();
//                message = inputtext.getText().toString();
                Log.d(TAG, "onClick: ============================================");
                recievefile.execute();
                if(recievefile.getStatus() == AsyncTask.Status.FINISHED) {
                    // My AsyncTask is done and onPostExecute was called
                    textView.setText("Sent");
                }
            }
        });

    }


    class send extends AsyncTask<Void, Void, Void> {

        Socket s;
        PrintWriter pw;
        private static final String TAG = "t";

        @SuppressLint("WrongThread")
        @Override
        protected Void doInBackground(Void...params){

            try{

                s = new Socket("192.168.0.4",5000);

//                File file = new File(videoUri.toString());
//                Environment.getExternalStorageDirectory().getAbsolutePath()
//                File file = new File(Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DCIM),
//                        videoUri.toString());
                File file = new File(Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DCIM),
                        "/Camera/VID_20200222_163752.mp4"); // works


//                File file = new File("storage/DCIM/Camera/VID_20191222_112747.mp4");
//                File musicDirectory = new File(Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DCIM));

                // Get the size of the file
                Log.d(TAG, "doInBackground: ===========================" + file.toString());
                long length = file.length();
                byte[] bytes = new byte[16 * 1024];

                InputStream in = new FileInputStream(file);
                OutputStream out = s.getOutputStream();

                int count;
                int i=0;
                while ((count = in.read(bytes)) > 0) {
                    out.write(bytes, 0, count);
                    Log.d(TAG, "doInBackground: ================" + i);
                    i+=1;
                }

//                textView.setText("sent");

                out.close();
                in.close();
                s.close();


            } catch (UnknownHostException e) {
                System.out.println("Fail");
                e.printStackTrace();
            } catch (IOException e) {
                System.out.println("Fail");
//                System.out.println(ip);
                e.printStackTrace();
            }
            return null;
        }
    }

    class recieve extends AsyncTask<Void, Void, Void>{

        Socket s;


        @Override
        protected Void doInBackground(Void... voids) {
            try{

                s = new Socket("192.168.0.4",5000);

                InputStream in = null;
                OutputStream out = null;


                try {
                    in = s.getInputStream();
                    Log.d(TAG, "doInBackground: Connected to the server");
                } catch (IOException ex) {
                    System.out.println("Can't get socket input stream. ");
                }

                //Create a new file that points to the root directory, with the given name:
                File file = new File(Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DCIM),
                        "/Camera/pcd.ply");




                try {
                    out = new FileOutputStream(file);
                    Log.d(TAG, "doInBackground: Output file found");
                } catch (FileNotFoundException ex) {
                    System.out.println("File not found. ");
                }

                byte[] bytes = new byte[16*1024];

                int count;
                Log.d(TAG, "doInBackground: Starting to write to file");
                while ((count = in.read(bytes)) > 0) {
                    Log.d(TAG, "doInBackground: Started");
                    out.write(bytes, 0, count);
                    Log.d(TAG, "doInBackground: recieving");
                }

                out.close();
                in.close();
                s.close();

            } catch (UnknownHostException e) {
                System.out.println("Fail");
                e.printStackTrace();
            } catch (IOException e) {
                System.out.println("Fail");
//                System.out.println(ip);
                e.printStackTrace();
            }
            return null;
        }
    }

//    @Override
//    protected void onProgressUpdate(String item) {
//        // text1.setText(item[0]);
//    }
//
//    @Override
//    protected void onPostExecute(Void unused) {
//        //Toast.makeText(GameScreen_bugfix.this, "music loaded!", Toast.LENGTH_SHORT).show();
//    }




    /**
     * Checks if the app has permission to write to device storage
     *
     * If the app does not has permission then the user will be prompted to grant permissions
     *
     * @param activity
     */
    public static void verifyStoragePermissions(Activity activity) {
        // Check if we have write permission
        int permission = ActivityCompat.checkSelfPermission(activity, Manifest.permission.WRITE_EXTERNAL_STORAGE);

        if (permission != PackageManager.PERMISSION_GRANTED) {
            // We don't have permission so prompt the user
            ActivityCompat.requestPermissions(
                    activity,
                    PERMISSIONS_STORAGE,
                    REQUEST_EXTERNAL_STORAGE
            );
        }
    }
}
