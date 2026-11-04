package app.enotone.icontest;

    import android.app.Activity;
    import android.os.Bundle;
    import android.graphics.Color;
    import android.graphics.Typeface;
    import android.graphics.drawable.Drawable;
    import android.widget.LinearLayout;
    import android.widget.ScrollView;
    import android.widget.TextView;
    import android.widget.ImageView;
    import android.view.Gravity;
    import android.util.TypedValue;

    public final class MainActivity extends Activity {
        private int dp(float n) { return (int)(n * getResources().getDisplayMetrics().density + 0.5f); }
        private TextView text(String t, int sp, boolean bold) {
            TextView v = new TextView(this);
            v.setText(t);
            v.setTextColor(Color.rgb(33,30,28));
            v.setTextSize(TypedValue.COMPLEX_UNIT_SP, sp);
            if (bold) v.setTypeface(Typeface.DEFAULT, Typeface.BOLD);
            v.setPadding(0,dp(7),0,dp(7));
            return v;
        }
        private LinearLayout vertical() {
            LinearLayout l = new LinearLayout(this);l.setOrientation(LinearLayout.VERTICAL);return l;
        }
        private void preview(LinearLayout parent,String title,int res) {
            LinearLayout row = new LinearLayout(this);
            row.setGravity(Gravity.CENTER_VERTICAL);
            ImageView icon=new ImageView(this);
            icon.setImageResource(res);
            row.addView(icon,new LinearLayout.LayoutParams(dp(90),dp(90)));
            TextView t=text(title,16,false);
            t.setPadding(dp(14),0,0,0);
            row.addView(t);
            row.setPadding(0,dp(5),0,dp(5));
            parent.addView(row);
        }
        @Override public void onCreate(Bundle b) {
            super.onCreate(b);
            ScrollView scroll=new ScrollView(this);
            LinearLayout c=vertical(); c.setPadding(dp(20),dp(24),dp(20),dp(24));
            c.setBackgroundColor(Color.rgb(237,233,229));
            scroll.addView(c);
            c.addView(text("enoTone — проверка иконки",22,true));
            String alias=(getIntent()!=null && getIntent().getComponent()!=null) ? getIntent().getComponent().getShortClassName() : "не определён";
            c.addView(text("Открыта иконка: " + alias,13,false));
            c.addView(text("На рабочем столе появятся шесть значков: четыре утверждённых PNG и два адаптивных кандидата. Это намеренно — для сравнения масок EMUI.",15,false));
            c.addView(text("Адаптивные кандидаты",18,true));
            preview(c,"Графит · прозрачный foreground",R.mipmap.adaptive_graphite);
            preview(c,"Фарфор · прозрачный foreground",R.mipmap.adaptive_porcelain);
            c.addView(text("Оригинальные изображения (PNG)",18,true));
            preview(c,"Графит · квадрат",R.mipmap.legacy_graphite_square);
            preview(c,"Графит · круг",R.mipmap.legacy_graphite_round);
            preview(c,"Фарфор · квадрат",R.mipmap.legacy_porcelain_square);
            preview(c,"Фарфор · круг",R.mipmap.legacy_porcelain_round);
            c.addView(text("ПРОВЕРЬ НА РАБОЧЕМ СТОЛЕ:",17,true));
            c.addView(text("1. Видны ли шесть отдельных значков?\n2. Не обрезает ли EMUI уши и направленный палец?\n3. Касается ли Бандит нижнего края?\n4. Нет ли ореолов вокруг шерсти и шарфа?\n5. Как выглядят светлый и тёмный варианты после перезагрузки лаунчера?",15,false));
            c.addView(text("Тестовое приложение. Не играет музыку, не использует сеть, не содержит учетных данных.",12,false));
            setContentView(scroll);
        }
    }
