package com.example.okhttp_example;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import java.io.IOException;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class post_get extends AppCompatActivity {
    class we{
        String ss="666";
        public void setSs(String s){
            ss = s;
        }
        public String getSs(){
            return ss;
        }


    };



    private EditText input_ur;
    private Button get;
    private Button post;
    private TextView respons;
    private we temp = new we();

    private final OkHttpClient client = new OkHttpClient();

    public void run(String str) throws Exception {
        Request request = new Request.Builder()
                .url(str)
                .build();
            client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                // Throwable.printStackTrace();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                if (!response.isSuccessful()) throw new IOException("Unexpected code " + response);
                String ss = new String(response.body().string().toCharArray(),0,5);
                final String s2 =ss;
                temp.setSs(ss);
                //respons.setText(s2);
                System.out.println(ss);
            }


        });
    }
    View.OnClickListener get_press = new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            //run((String) R.string.input_http);
            //
            String s = input_ur.getText().toString();
            try {
                run(s);
            } catch (Exception e) {
                e.printStackTrace();
            }
            respons.setText(s);
            Toast.makeText(getApplicationContext(),temp.getSs(),Toast.LENGTH_LONG).show();
            System.out.print(s);
        }

    };
    View.OnClickListener post_press = new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            //
            Toast toast = Toast.makeText(getApplicationContext(),"gay",Toast.LENGTH_LONG);
            toast.show();
        }
    };






    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_post_get);



        input_ur = findViewById(R.id.url_in);
        get = findViewById(R.id.get_b);
        post = findViewById(R.id.post_b);
        get.setOnClickListener(get_press);
        post.setOnClickListener(post_press);
        respons = findViewById(R.id.response);
    }
}
